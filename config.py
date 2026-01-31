import os

class Config:
    """Application configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    UPLOAD_FOLDER = 'uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    ALLOWED_EXTENSIONS = {'csv', 'pdf'}
    DATABASE_PATH = 'fintech_app.db'
    
    # Mock AI settings
    MOCK_AI_ENABLED = True
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')  # For future integration
