import os

class Config:
    # Get SECRET_KEY from environment or use default for development
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev_secret_key_replace_in_production')
    
    # Set DEBUG based on environment
    DEBUG = os.environ.get('ENVIRONMENT', 'development') == 'development'

    # Fitbit API credentials
    CLIENT_ID = os.environ.get('CLIENT_ID', '23QCSZ')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET', '4112a6a244bf91db710ff2580f2be515')
    
    # Auth URLs
    AUTH_URL = "https://www.fitbit.com/oauth2/authorize"
    TOKEN_URL = "https://api.fitbit.com/oauth2/token"
    API_BASE_URL = "https://api.fitbit.com/1/user/-/"
    
    # Dynamic REDIRECT_URI based on environment
    VERCEL_URL = os.environ.get('VERCEL_URL', '')
    
    # If running on Vercel, use the Vercel URL, otherwise use localhost
    if VERCEL_URL:
        REDIRECT_URI = f"https://{VERCEL_URL}/callback"
    else:
        REDIRECT_URI = os.environ.get('REDIRECT_URI', 'http://localhost:5000/callback')
