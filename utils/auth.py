import base64
import requests
import os
from config import Config

def authorize_user():
    client_id = os.environ.get('CLIENT_ID', Config.CLIENT_ID)
    redirect_uri = os.environ.get('REDIRECT_URI', Config.REDIRECT_URI)
    
    return (
        f"{Config.AUTH_URL}?response_type=code"
        f"&client_id={client_id}"
        f"&redirect_uri={redirect_uri}"
        f"&scope=activity heartrate sleep profile"
    )

def get_token(auth_code):
    token_url = Config.TOKEN_URL
    client_id = os.environ.get('CLIENT_ID', Config.CLIENT_ID)
    client_secret = os.environ.get('CLIENT_SECRET', Config.CLIENT_SECRET)
    redirect_uri = os.environ.get('REDIRECT_URI', Config.REDIRECT_URI)

    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "client_id": client_id,
        "grant_type": "authorization_code",
        "redirect_uri": redirect_uri,
        "code": auth_code
    }

    try:
        response = requests.post(token_url, headers=headers, data=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e), "details": str(e.response.text) if hasattr(e, 'response') else "No response details"}
