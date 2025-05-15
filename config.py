class Config:
    SECRET_KEY = 'your_secret_key'  
    DEBUG = True

    CLIENT_ID = "23QCSZ"
    CLIENT_SECRET = "4112a6a244bf91db710ff2580f2be515"
    
    # Update these URLs for production
    REDIRECT_URI = "https://your-vercel-app.vercel.app/callback"
    FRONTEND_URL = "https://your-frontend-app.vercel.app"

    AUTH_URL = "https://www.fitbit.com/oauth2/authorize"
    TOKEN_URL = "https://api.fitbit.com/oauth2/token"
    API_BASE_URL = "https://api.fitbit.com/1/user/-/"
