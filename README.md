# FinTech Portfolio Manager MVP

A Flask-based web application for lenders to manage investment portfolios with AI-powered insights and a buy-only marketplace.

## Features

### 1. Portfolio Management
- Upload CSV files with investment data
- View portfolio in sortable data table
- Real-time summary statistics (Total Invested, Average ROI, Asset Count)
- Session-based data storage with SQLite

### 2. AI Insights Dashboard
- Interactive Plotly charts:
  - **Line Chart**: Performance over time (ROI by Date)
  - **Pie Chart**: Sector breakdown
  - **Bar Chart**: Investments by Location
- Investment thesis analysis (mock AI)
- Risk profile assessment
- Personalized recommendations

### 3. Investment Marketplace
- Browse 8 curated investment bundles
- AI-ranked bundles based on portfolio and thesis
- Mini performance charts for each bundle
- One-click purchase flow

## Tech Stack

- **Backend**: Flask (Python)
- **Data Processing**: Pandas
- **Database**: SQLite
- **Frontend**: Bootstrap 5
- **Dynamic Updates**: HTMX
- **Charts**: Plotly.js
- **AI**: Mock responses (OpenAI API placeholder)

## Installation

1. **Clone or navigate to the project directory**

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Run the application**:
```bash
python app.py
```

4. **Open your browser** and navigate to:
```
http://localhost:5000
```

## Usage

### Getting Started

1. **Upload Portfolio**: 
   - Go to the Portfolio page
   - Upload the sample CSV file: `data/UKFIN_combined_dataset_FINAL.csv`
   - View your portfolio data in the interactive table

2. **View Insights**:
   - Navigate to the Insights page
   - Enter your investment thesis (optional)
   - Explore interactive charts and AI recommendations

3. **Browse Marketplace**:
   - Visit the Marketplace page
   - View AI-ranked investment bundles
   - Click "Buy Bundle" to proceed to checkout

### CSV Format

Your portfolio CSV should have the following columns:
- `ID`: Asset identifier
- `Asset`: Asset name
- `Sector`: Investment sector
- `Location`: Geographic location
- `Invested`: Amount invested (numeric)
- `ROI`: Return on investment percentage (numeric)
- `Date`: Investment date (YYYY-MM-DD)

## Project Structure

```
.
├── app.py                  # Main Flask application
├── config.py              # Configuration settings
├── database.py            # SQLite database utilities
├── models.py              # Data models and mock generators
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates
│   ├── base.html         # Base layout
│   ├── portfolio.html    # Portfolio management
│   ├── insights.html     # AI insights dashboard
│   ├── marketplace.html  # Investment marketplace
│   └── checkout.html     # Purchase checkout
├── static/
│   └── css/
│       └── style.css     # Custom styling
├── data/
│   └── UKFIN_combined_dataset_FINAL.csv  # Sample data
└── uploads/              # User uploaded files
```

## Features in Detail

### Portfolio View
- **CSV Upload**: Drag-and-drop or browse to upload
- **Data Validation**: Ensures required columns are present
- **Summary Cards**: Visual display of key metrics
- **Sortable Table**: Click column headers to sort

### Insights Dashboard
- **Performance Chart**: Track ROI trends over time
- **Sector Analysis**: Visualize investment distribution
- **Location Breakdown**: Geographic investment spread
- **AI Recommendations**: Mock AI-generated insights based on portfolio composition

### Marketplace
- **Bundle Cards**: Rich display of investment opportunities
- **AI Ranking**: Bundles ranked by match score
- **Preview Charts**: Mini performance visualizations
- **Quick Purchase**: Streamlined checkout process

## Mock AI Features

The application includes placeholder AI functionality:
- Risk profile assessment
- Portfolio diversification scoring
- Sector-based recommendations
- Bundle ranking by thesis match

To integrate real AI (OpenAI GPT-4):
1. Set `OPENAI_API_KEY` environment variable
2. Update `models.py` to call OpenAI API
3. Set `MOCK_AI_ENABLED = False` in `config.py`

## Development Notes

- **Session Management**: Uses Flask sessions with unique IDs
- **Database**: SQLite for lightweight data persistence
- **Responsive Design**: Mobile-friendly Bootstrap layout
- **HTMX Integration**: Enables dynamic updates without page reloads
- **Security**: File upload validation and secure filename handling

## Future Enhancements

- Real OpenAI API integration
- User authentication and multi-user support
- Advanced portfolio analytics
- Real-time market data integration
- Transaction history and audit logs
- Export reports (PDF/Excel)

## License

This is an MVP for demonstration purposes.

## Support

For questions or issues, please contact the development team.
