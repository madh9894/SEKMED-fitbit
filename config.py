class Config:
    SECRET_KEY = 'your_secret_key'  
    DEBUG = False  # Set to False for production

    # These should be set as environment variables in Vercel
    CLIENT_ID = "23QCSZ"
    CLIENT_SECRET = "4112a6a244bf91db710ff2580f2be515"
    
    # Update this to your Vercel deployment URL
    REDIRECT_URI = "https://your-app-name.vercel.app/callback"

    AUTH_URL = "https://www.fitbit.com/oauth2/authorize"
    TOKEN_URL = "https://api.fitbit.com/oauth2/token"
    API_BASE_URL = "https://api.fitbit.com/1/user/-/"
