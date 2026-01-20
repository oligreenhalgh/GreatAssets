from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
from services.supabase_client import get_supabase_client
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "supersecretkey")

@app.route('/')
def index():
    data = []
    try:
        supabase = get_supabase_client()
        # Replace 'your_table_name' with your actual table name
        response = supabase.table('your_table_name').select("*").execute()
        data = response.data
    except Exception as e:
        print(f"Error fetching data: {e}")
        # In production, handle this more gracefully
        
    return render_template('index.html', data=data)

@app.route('/submit', methods=['POST'])
def submit():
    payload = request.form.get('payload')
    if payload:
        try:
            supabase = get_supabase_client()
            # Replace 'your_table_name' with your actual table name
            supabase.table('your_table_name').insert({"payload": payload}).execute()
            flash("Data submitted successfully!", "success")
        except Exception as e:
            print(f"Error inserting data: {e}")
            flash("Error submitting data.", "danger")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
