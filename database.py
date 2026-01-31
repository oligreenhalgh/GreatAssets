import sqlite3
from config import Config

def init_db():
    """Initialize the SQLite database"""
    conn = sqlite3.connect(Config.DATABASE_PATH)
    cursor = conn.cursor()
    
    # Create portfolio table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS portfolio (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_id TEXT,
            asset TEXT,
            sector TEXT,
            location TEXT,
            invested REAL,
            roi REAL,
            date TEXT,
            session_id TEXT
        )
    ''')
    
    # Create user preferences table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS preferences (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT,
            thesis TEXT,
            risk_profile TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

def get_db_connection():
    """Get database connection"""
    conn = sqlite3.connect(Config.DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def save_portfolio_data(df, session_id):
    """Save portfolio DataFrame to database"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Clear existing data for this session
    cursor.execute('DELETE FROM portfolio WHERE session_id = ?', (session_id,))
    
    # Insert new data
    for _, row in df.iterrows():
        cursor.execute('''
            INSERT INTO portfolio (asset_id, asset, sector, location, invested, roi, date, session_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            str(row.get('ID', '')),
            str(row.get('Asset', '')),
            str(row.get('Sector', '')),
            str(row.get('Location', '')),
            float(row.get('Invested', 0)),
            float(row.get('ROI', 0)),
            str(row.get('Date', '')),
            session_id
        ))
    
    conn.commit()
    conn.close()

def get_portfolio_data(session_id):
    """Retrieve portfolio data for a session"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM portfolio WHERE session_id = ?', (session_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def save_thesis(session_id, thesis, risk_profile):
    """Save investment thesis and risk profile"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM preferences WHERE session_id = ?', (session_id,))
    cursor.execute('''
        INSERT INTO preferences (session_id, thesis, risk_profile)
        VALUES (?, ?, ?)
    ''', (session_id, thesis, risk_profile))
    
    conn.commit()
    conn.close()

def get_thesis(session_id):
    """Retrieve thesis for a session"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM preferences WHERE session_id = ?', (session_id,))
    row = cursor.fetchone()
    conn.close()
    return row
