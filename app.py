from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from werkzeug.utils import secure_filename
import pandas as pd
import os
import json
from datetime import datetime
import uuid

from config import Config
from database import init_db, save_portfolio_data, get_portfolio_data, save_thesis, get_thesis
from models import generate_mock_bundles, generate_ai_insights, rank_bundles_by_thesis, generate_sample_csv_data

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
init_db()

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def get_session_id():
    """Get or create session ID"""
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())
    return session['session_id']

@app.route('/')
def index():
    """Home page - redirect to portfolio"""
    return redirect(url_for('portfolio'))

@app.route('/portfolio', methods=['GET', 'POST'])
def portfolio():
    """Portfolio management page - auto-loads UKFIN data"""
    session_id = get_session_id()
    portfolio_data = None
    summary_stats = None
    
    # Check if data already loaded in session
    rows = get_portfolio_data(session_id)
    
    # If no data in session, auto-load from CSV
    if not rows:
        try:
            csv_path = os.path.join('data', 'UKFIN_combined_dataset_FINAL.csv')
            df = pd.read_csv(csv_path)
            
            # Save to database
            save_portfolio_data(df, session_id)
            rows = get_portfolio_data(session_id)
        except Exception as e:
            flash(f'Error loading portfolio data: {str(e)}', 'error')
    
    if rows:
        portfolio_data = [dict(row) for row in rows]
        
        # Calculate summary statistics
        total_invested = sum(row['invested'] for row in portfolio_data)
        avg_roi = sum(row['roi'] for row in portfolio_data) / len(portfolio_data)
        asset_count = len(portfolio_data)
        
        summary_stats = {
            'total_invested': f"£{total_invested:,.2f}",
            'avg_roi': f"{avg_roi:.2f}%",
            'asset_count': asset_count
        }
    
    return render_template('portfolio.html', 
                         portfolio=portfolio_data, 
                         summary=summary_stats)

@app.route('/insights', methods=['GET', 'POST'])
def insights():
    """Insights dashboard with charts and AI analysis"""
    session_id = get_session_id()
    
    # Get portfolio data
    rows = get_portfolio_data(session_id)
    
    if not rows:
        flash('Please visit the portfolio page first to load data', 'warning')
        return redirect(url_for('portfolio'))
    
    portfolio_data = [dict(row) for row in rows]
    
    # Handle thesis file upload
    if request.method == 'POST':
        if 'thesis_file' in request.files:
            file = request.files['thesis_file']
            if file and file.filename:
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                
                # Read file content
                try:
                    if filename.endswith('.txt'):
                        with open(filepath, 'r') as f:
                            thesis_text = f.read()
                    elif filename.endswith('.pdf'):
                        # For PDF, we'll use a placeholder since we don't have PyPDF2
                        thesis_text = "PDF content extracted (placeholder)"
                    else:
                        thesis_text = "Uploaded file content"
                    
                    # Extract risk profile (mock AI)
                    risk_profile = 'Moderate-Aggressive'
                    save_thesis(session_id, thesis_text, risk_profile)
                    flash('Investment thesis uploaded and analyzed!', 'success')
                except Exception as e:
                    flash(f'Error reading file: {str(e)}', 'error')
    
    # Check for default thesis if none uploaded
    thesis_data = get_thesis(session_id)
    if not thesis_data:
        # Load default thesis
        default_thesis_path = os.path.join('data', 'investment_thesis.txt')
        if os.path.exists(default_thesis_path):
            with open(default_thesis_path, 'r') as f:
                default_text = f.read()
            save_thesis(session_id, default_text, 'Moderate-Aggressive')
            thesis_data = get_thesis(session_id)
    
    thesis_text = thesis_data['thesis'] if thesis_data else None
    
    # Generate AI summary of thesis
    ai_summary = None
    if thesis_text:
        # Mock AI summary extraction
        ai_summary = {
            'risk_profile': thesis_data['risk_profile'] if thesis_data else 'Moderate',
            'key_sectors': ['Technology & Fintech (35%)', 'Renewable Energy (20%)', 'Healthcare & Biotech (15%)'],
            'target_roi': '14-16% annually',
            'investment_horizon': '5-7 years',
            'geographic_focus': 'UK (London, Edinburgh, Cambridge, Manchester)',
            'strategy': 'Balanced growth across emerging and established sectors with quarterly rebalancing'
        }
    
    # Generate AI insights
    ai_insights = generate_ai_insights(portfolio_data, thesis_text)
    
    # Prepare chart data
    df = pd.DataFrame(portfolio_data)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    
    performance_data = {
        'dates': df['date'].dt.strftime('%Y-%m-%d').tolist(),
        'roi': df['roi'].tolist(),
        'assets': df['asset'].tolist()
    }
    
    sector_counts = df.groupby('sector')['invested'].sum().to_dict()
    sector_data = {
        'labels': list(sector_counts.keys()),
        'values': list(sector_counts.values())
    }
    
    location_counts = df.groupby('location')['invested'].sum().to_dict()
    location_data = {
        'labels': list(location_counts.keys()),
        'values': list(location_counts.values())
    }
    
    return render_template('insights.html',
                         performance_data=json.dumps(performance_data),
                         sector_data=json.dumps(sector_data),
                         location_data=json.dumps(location_data),
                         ai_insights=ai_insights,
                         ai_summary=ai_summary,
                         has_thesis=thesis_data is not None)

@app.route('/marketplace/buy')
def marketplace_buy():
    """Marketplace page with investment bundles"""
    session_id = get_session_id()
    
    # Get portfolio data for AI ranking
    rows = get_portfolio_data(session_id)
    portfolio_sectors = None
    
    if rows:
        portfolio_data = [dict(row) for row in rows]
        df = pd.DataFrame(portfolio_data)
        portfolio_sectors = df['sector'].value_counts().to_dict()
    
    # Get thesis for ranking
    thesis_data = get_thesis(session_id)
    thesis_text = thesis_data['thesis'] if thesis_data else None
    
    # Generate and rank bundles
    bundles = generate_mock_bundles()
    
    # Generate AI recommendations for each bundle
    from models import generate_bundle_recommendations
    bundles = generate_bundle_recommendations(bundles, thesis_text, portfolio_sectors)
    
    # Rank bundles
    ranked_bundles = rank_bundles_by_thesis(bundles, thesis_text, portfolio_sectors)
    
    return render_template('marketplace.html', bundles=ranked_bundles)

@app.route('/checkout/<int:bundle_id>')
def checkout(bundle_id):
    """Checkout page for selected bundle"""
    bundles = generate_mock_bundles()
    bundle = next((b for b in bundles if b.id == bundle_id), None)
    
    if not bundle:
        flash('Bundle not found', 'error')
        return redirect(url_for('marketplace_buy'))
    
    return render_template('checkout.html', bundle=bundle)

@app.route('/api/sample-data')
def api_sample_data():
    """API endpoint to download sample CSV data"""
    sample_data = generate_sample_csv_data()
    df = pd.DataFrame(sample_data)
    
    # Save to uploads folder
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'UKFIN_combined_dataset_FINAL.csv')
    df.to_csv(filepath, index=False)
    
    return jsonify({'message': 'Sample data generated', 'path': filepath})

@app.route('/view-thesis')
def view_thesis():
    """Serve the investment thesis file"""
    session_id = get_session_id()
    thesis_data = get_thesis(session_id)
    
    if thesis_data:
        return f"<pre style='padding: 20px; font-family: monospace; white-space: pre-wrap;'>{thesis_data['thesis']}</pre>"
    else:
        return "No thesis uploaded yet", 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)
