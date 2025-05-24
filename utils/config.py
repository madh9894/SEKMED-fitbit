import os

class Config:
    # Get environment variables with fallbacks for local development
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_local_secret_key')
    
    # Fitbit API settings
    CLIENT_ID = os.environ.get('FITBIT_CLIENT_ID', '23QCSZ')
    CLIENT_SECRET = os.environ.get('FITBIT_CLIENT_SECRET', '4112a6a244bf91db710ff2580f2be515')
    
    # Use environment variables for URLs in production
    REDIRECT_URI = os.environ.get('REDIRECT_URI', 'http://localhost:5000/callback')
    FRONTEND_URL = os.environ.get('FRONTEND_URL', 'https://sekmed.vercel.app')
    
    # Fitbit API endpoints
    AUTH_URL = "https://www.fitbit.com/oauth2/authorize"
    TOKEN_URL = "https://api.fitbit.com/oauth2/token"
    API_BASE_URL = "https://api.fitbit.com/1/user/-/"

