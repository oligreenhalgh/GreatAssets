import random
from datetime import datetime, timedelta

class InvestmentBundle:
    """Model for investment bundles in marketplace"""
    def __init__(self, bundle_id, title, sector, roi, location, revenue, description, assets, detailed_assets=None, ai_recommendation=None):
        self.id = bundle_id
        self.title = title
        self.sector = sector
        self.roi = roi
        self.location = location
        self.revenue = revenue
        self.description = description
        self.assets = assets
        self.detailed_assets = detailed_assets or []
        self.ai_recommendation = ai_recommendation or {}

def generate_mock_bundles():
    """Generate mock investment bundles for marketplace"""
    bundles = [
        InvestmentBundle(
            bundle_id=1,
            title="UK Tech Growth Portfolio",
            sector="Technology",
            roi=18.5,
            location="London",
            revenue=2500000,
            description="High-growth tech startups in fintech and AI sectors",
            assets=["FinTech Innovate Ltd", "AI Solutions UK", "CloudTech Partners"],
            detailed_assets=[
                {"id": "TECH001", "sector": "Technology", "location": "London", "loan_band": "£500k-750k", "roi_band": "High (15%+)", "risk": "Low Risk"},
                {"id": "TECH002", "sector": "Technology", "location": "London", "loan_band": "£250k-500k", "roi_band": "High (15%+)", "risk": "Low Risk"},
                {"id": "TECH003", "sector": "Technology", "location": "Cambridge", "loan_band": "£250k-500k", "roi_band": "Medium (10-15%)", "risk": "Medium Risk"}
            ]
        ),
        InvestmentBundle(
            bundle_id=2,
            title="Renewable Energy Fund",
            sector="Energy",
            roi=12.3,
            location="Scotland",
            revenue=5000000,
            description="Diversified renewable energy projects including wind and solar",
            assets=["ScotWind Energy", "Solar Farms Ltd", "Green Power Co"],
            detailed_assets=[
                {"id": "ENRG001", "sector": "Energy", "location": "Scotland", "loan_band": "£750k+", "roi_band": "Medium (10-15%)", "risk": "Medium Risk"},
                {"id": "ENRG002", "sector": "Energy", "location": "Scotland", "loan_band": "£500k-750k", "roi_band": "Medium (10-15%)", "risk": "Medium Risk"},
                {"id": "ENRG003", "sector": "Energy", "location": "Wales", "loan_band": "£250k-500k", "roi_band": "Low (0-10%)", "risk": "High Risk"}
            ]
        ),
        InvestmentBundle(
            bundle_id=3,
            title="Healthcare Innovation",
            sector="Healthcare",
            roi=15.7,
            location="Cambridge",
            revenue=3200000,
            description="Biotech and medical device companies with strong IP",
            assets=["BioMed Research", "MedTech Devices", "HealthAI Systems"],
            detailed_assets=[
                {"id": "HLTH001", "sector": "Healthcare", "location": "Cambridge", "loan_band": "£500k-750k", "roi_band": "High (15%+)", "risk": "Low Risk"},
                {"id": "HLTH002", "sector": "Healthcare", "location": "Oxford", "loan_band": "£250k-500k", "roi_band": "High (15%+)", "risk": "Low Risk"},
                {"id": "HLTH003", "sector": "Healthcare", "location": "Cambridge", "loan_band": "£250k-500k", "roi_band": "Medium (10-15%)", "risk": "Medium Risk"}
            ]
        ),
        InvestmentBundle(
            bundle_id=4,
            title="Real Estate Development",
            sector="Real Estate",
            roi=10.2,
            location="Manchester",
            revenue=8000000,
            description="Commercial and residential property development projects",
            assets=["Urban Developments", "Property Partners", "City Estates"],
            detailed_assets=[
                {"id": "REST001", "sector": "Real Estate", "location": "Manchester", "loan_band": "£750k+", "roi_band": "Medium (10-15%)", "risk": "Medium Risk"},
                {"id": "REST002", "sector": "Real Estate", "location": "Birmingham", "loan_band": "£750k+", "roi_band": "Low (0-10%)", "risk": "High Risk"},
                {"id": "REST003", "sector": "Real Estate", "location": "Manchester", "loan_band": "£500k-750k", "roi_band": "Low (0-10%)", "risk": "High Risk"}
            ]
        ),
        InvestmentBundle(
            bundle_id=5,
            title="Consumer Goods Expansion",
            sector="Consumer",
            roi=14.1,
            location="Birmingham",
            revenue=4500000,
            description="Established consumer brands with expansion plans",
            assets=["Brand Collective", "Consumer Goods Ltd", "Retail Innovations"],
            detailed_assets=[
                {"id": "CONS001", "sector": "Consumer", "location": "Birmingham", "loan_band": "£500k-750k", "roi_band": "Medium (10-15%)", "risk": "Medium Risk"},
                {"id": "CONS002", "sector": "Consumer", "location": "Leeds", "loan_band": "£250k-500k", "roi_band": "Medium (10-15%)", "risk": "Medium Risk"},
                {"id": "CONS003", "sector": "Consumer", "location": "Birmingham", "loan_band": "£250k-500k", "roi_band": "High (15%+)", "risk": "Low Risk"}
            ]
        ),
        InvestmentBundle(
            bundle_id=6,
            title="Financial Services Suite",
            sector="Finance",
            roi=16.8,
            location="Edinburgh",
            revenue=6000000,
            description="Digital banking and insurance technology platforms",
            assets=["Digital Bank Pro", "InsurTech Solutions", "Payment Systems"],
            detailed_assets=[
                {"id": "FINC001", "sector": "Finance", "location": "Edinburgh", "loan_band": "£750k+", "roi_band": "High (15%+)", "risk": "Low Risk"},
                {"id": "FINC002", "sector": "Finance", "location": "London", "loan_band": "£500k-750k", "roi_band": "High (15%+)", "risk": "Low Risk"},
                {"id": "FINC003", "sector": "Finance", "location": "Edinburgh", "loan_band": "£250k-500k", "roi_band": "Medium (10-15%)", "risk": "Medium Risk"}
            ]
        ),
        InvestmentBundle(
            bundle_id=7,
            title="Manufacturing Modernization",
            sector="Manufacturing",
            roi=11.5,
            location="Leeds",
            revenue=3800000,
            description="Advanced manufacturing with automation and IoT integration",
            assets=["Smart Factory Ltd", "AutoMate Systems", "Industrial IoT"],
            detailed_assets=[
                {"id": "MANF001", "sector": "Manufacturing", "location": "Leeds", "loan_band": "£500k-750k", "roi_band": "Medium (10-15%)", "risk": "Medium Risk"},
                {"id": "MANF002", "sector": "Manufacturing", "location": "Sheffield", "loan_band": "£250k-500k", "roi_band": "Medium (10-15%)", "risk": "Medium Risk"},
                {"id": "MANF003", "sector": "Manufacturing", "location": "Leeds", "loan_band": "£250k-500k", "roi_band": "Low (0-10%)", "risk": "High Risk"}
            ]
        ),
        InvestmentBundle(
            bundle_id=8,
            title="Education Technology",
            sector="Education",
            roi=13.9,
            location="Oxford",
            revenue=2100000,
            description="Online learning platforms and educational software",
            assets=["EduTech Platform", "Learning Systems", "Virtual Academy"],
            detailed_assets=[
                {"id": "EDUC001", "sector": "Education", "location": "Oxford", "loan_band": "£250k-500k", "roi_band": "Medium (10-15%)", "risk": "Medium Risk"},
                {"id": "EDUC002", "sector": "Education", "location": "London", "loan_band": "£250k-500k", "roi_band": "Medium (10-15%)", "risk": "Medium Risk"},
                {"id": "EDUC003", "sector": "Education", "location": "Cambridge", "loan_band": "£0-250k", "roi_band": "High (15%+)", "risk": "Low Risk"}
            ]
        )
    ]
    return bundles

def generate_ai_insights(portfolio_data, thesis=None):
    """Generate mock AI insights based on portfolio"""
    insights = {
        'risk_profile': random.choice(['Conservative', 'Moderate', 'Aggressive']),
        'recommendations': [],
        'sector_analysis': {},
        'diversification_score': random.randint(60, 95)
    }
    
    # Mock recommendations
    recommendations = [
        {
            'title': 'Sector Diversification',
            'message': 'Your portfolio is heavily weighted in Technology (35%). Consider diversifying into Energy or Healthcare sectors.',
            'priority': 'high'
        },
        {
            'title': 'Geographic Expansion',
            'message': 'Strong concentration in London-based assets. Explore opportunities in Scotland and Northern England.',
            'priority': 'medium'
        },
        {
            'title': 'ROI Optimization',
            'message': 'Average portfolio ROI is 14.2%. Consider rebalancing towards higher-performing sectors like Finance (16.8% avg).',
            'priority': 'medium'
        },
        {
            'title': 'Risk Management',
            'message': 'Current risk profile is Moderate. Your thesis suggests alignment with growth opportunities in emerging sectors.',
            'priority': 'low'
        }
    ]
    
    insights['recommendations'] = random.sample(recommendations, 3)
    
    return insights

def rank_bundles_by_thesis(bundles, thesis=None, portfolio_sectors=None):
    """Mock AI ranking of bundles based on thesis and portfolio"""
    # Simple mock ranking - in production would use actual AI
    ranked = bundles.copy()
    
    # If portfolio has sector data, deprioritize overweight sectors
    if portfolio_sectors:
        for bundle in ranked:
            if bundle.sector in portfolio_sectors:
                bundle.match_score = random.uniform(0.6, 0.8)
            else:
                bundle.match_score = random.uniform(0.8, 0.95)
    else:
        for bundle in ranked:
            bundle.match_score = random.uniform(0.7, 0.95)
    
    # Sort by match score
    ranked.sort(key=lambda x: x.match_score, reverse=True)
    
    return ranked

def generate_bundle_recommendations(bundles, thesis=None, portfolio_sectors=None):
    """Generate AI recommendations for each bundle based on thesis and portfolio gaps"""
    recommendations_map = {
        1: {  # UK Tech Growth Portfolio
            'why_recommended': 'This bundle aligns with your thesis emphasis on Technology & Fintech (35% target allocation). The high ROI potential (18.5%) exceeds your target range of 14-16% annually.',
            'gap_analysis': 'Addresses your underweight position in London-based fintech assets. Provides exposure to AI and cloud technologies, emerging sectors in your thesis.',
            'thesis_alignment': ['Technology sector growth focus', 'High ROI targets (15%+)', 'London geographic concentration']
        },
        2: {  # Renewable Energy Fund
            'why_recommended': 'Directly supports your Renewable Energy allocation target (20%). Scotland-based assets provide geographic diversification beyond London.',
            'gap_analysis': 'Fills critical gap in your renewable energy exposure. Thesis emphasizes green energy transition with government incentives - this bundle captures that opportunity.',
            'thesis_alignment': ['Renewable Energy 20% target', 'Geographic expansion to Scotland', 'Long-term revenue stability']
        },
        3: {  # Healthcare Innovation
            'why_recommended': 'Matches your Healthcare & Biotech allocation target (15%). Cambridge location leverages world-class biotech cluster mentioned in your thesis.',
            'gap_analysis': 'Strengthens portfolio diversification with healthcare exposure. High ROI (15.7%) aligns with growth-oriented return targets.',
            'thesis_alignment': ['Healthcare sector 15% allocation', 'Cambridge biotech cluster access', 'Strong IP protection framework']
        },
        4: {  # Real Estate Development
            'why_recommended': 'Provides exposure to your Real Estate allocation (10% target). Manchester and Birmingham focus supports thesis emphasis on high-growth urban areas.',
            'gap_analysis': 'Balances portfolio with established sector exposure. Lower ROI (10.2%) provides stability against higher-risk technology investments.',
            'thesis_alignment': ['Real Estate 10% allocation', 'Manchester/Birmingham development', 'Mixed-use regeneration zones']
        },
        5: {  # Consumer Goods Expansion
            'why_recommended': 'Addresses Consumer & Manufacturing allocation (5% target). Established brands provide portfolio stability with moderate growth potential.',
            'gap_analysis': 'Fills gap in consumer sector exposure. Birmingham location diversifies geographic concentration away from London.',
            'thesis_alignment': ['Consumer sector diversification', 'Established brand equity', 'Geographic expansion']
        },
        6: {  # Financial Services Suite
            'why_recommended': 'Strong fit for Financial Services allocation (15% target). High ROI (16.8%) exceeds portfolio average and thesis targets.',
            'gap_analysis': 'Edinburgh location provides Scottish exposure. Digital transformation focus aligns with thesis emphasis on fintech innovation.',
            'thesis_alignment': ['Financial Services 15% allocation', 'Digital transformation opportunities', 'High ROI potential']
        },
        7: {  # Manufacturing Modernization
            'why_recommended': 'Supports Manufacturing allocation within Consumer & Manufacturing category (5% target). Industry 4.0 focus aligns with thesis innovation emphasis.',
            'gap_analysis': 'Provides exposure to advanced manufacturing. Leeds location diversifies portfolio beyond London and Scotland.',
            'thesis_alignment': ['Manufacturing modernization', 'Industry 4.0 technologies', 'Northern England expansion']
        },
        8: {  # Education Technology
            'why_recommended': 'EdTech represents emerging opportunity sector. Oxford location provides access to education innovation hub.',
            'gap_analysis': 'Fills gap in education technology exposure. Moderate ROI (13.9%) with growth potential in digital learning sector.',
            'thesis_alignment': ['Emerging sector opportunities', 'Digital transformation', 'Oxford education cluster']
        }
    }
    
    for bundle in bundles:
        if bundle.id in recommendations_map:
            bundle.ai_recommendation = recommendations_map[bundle.id]
    
    return bundles

def generate_sample_csv_data():
    """Generate sample portfolio data for demo"""
    sectors = ['Technology', 'Energy', 'Healthcare', 'Finance', 'Real Estate', 'Consumer', 'Manufacturing']
    locations = ['London', 'Manchester', 'Edinburgh', 'Birmingham', 'Leeds', 'Cambridge', 'Oxford']
    
    data = []
    start_date = datetime(2023, 1, 1)
    
    for i in range(1, 21):
        data.append({
            'ID': f'AST{i:03d}',
            'Asset': f'Investment Asset {i}',
            'Sector': random.choice(sectors),
            'Location': random.choice(locations),
            'Invested': random.randint(50000, 500000),
            'ROI': round(random.uniform(5.0, 25.0), 2),
            'Date': (start_date + timedelta(days=random.randint(0, 730))).strftime('%Y-%m-%d')
        })
    
    return data
