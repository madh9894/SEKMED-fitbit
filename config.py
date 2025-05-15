import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
    DEBUG = os.environ.get('DEBUG', 'False') == 'True'

    CLIENT_ID = os.environ.get('CLIENT_ID', "23QCSZ")
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET', "4112a6a244bf91db710ff2580f2be515")
    
    # Update these URLs for production
    REDIRECT_URI = os.environ.get('REDIRECT_URI', "https://sekmed-fitbit.vercel.app/callback")
    FRONTEND_URL = os.environ.get('FRONTEND_URL', "https://sekmed-fitbit.vercel.app")

    AUTH_URL = "https://www.fitbit.com/oauth2/authorize"
    TOKEN_URL = "https://api.fitbit.com/oauth2/token"
    API_BASE_URL = "https://api.fitbit.com/1/user/-/"
