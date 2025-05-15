import base64
import requests
from config import Config

def authorize_user():
    return (
        f"{Config.AUTH_URL}?response_type=code"
        f"&client_id={Config.CLIENT_ID}"
        f"&redirect_uri={Config.REDIRECT_URI}"
        f"&scope=activity heartrate sleep profile"
    )

def get_token(auth_code):
    token_url = Config.TOKEN_URL
    redirect_uri = Config.REDIRECT_URI

    auth_header = base64.b64encode(f"{Config.CLIENT_ID}:{Config.CLIENT_SECRET}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "client_id": Config.CLIENT_ID,
        "grant_type": "authorization_code",
        "redirect_uri": redirect_uri,
        "code": auth_code
    }

    response = requests.post(token_url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()
