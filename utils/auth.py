import base64
import httpx
import os
from utils.config import Config

def authorize_user():
    """
    Generate authorization URL for Fitbit OAuth flow with forced re-authentication
    Returns:
        str: The complete authorization URL
    """
    # Define requested permission scopes
    scope = "activity heartrate profile sleep"

    # Construct authorization URL with parameters
    auth_url = (
        f"{Config.AUTH_URL}"
        f"?response_type=code"
        f"&client_id={Config.CLIENT_ID}"
        f"&redirect_uri={Config.REDIRECT_URI}"
        f"&scope={scope}"
        f"&expires_in=86400"  # Token valid for 24 hours only
        f"&prompt=login"  # Force re-authentication every time
    )
    return auth_url

async def get_token(code):
    """
    Exchange Fitbit OAuth 'code' for access/refresh token
    """
    import urllib.parse

    auth_header = base64.b64encode(f"{Config.CLIENT_ID}:{Config.CLIENT_SECRET}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "client_id": Config.CLIENT_ID,
        "grant_type": "authorization_code",
        "redirect_uri": Config.REDIRECT_URI,
        "code": code,
    }
    encoded_data = urllib.parse.urlencode(data)

    async with httpx.AsyncClient() as client:
        resp = await client.post(Config.TOKEN_URL, data=encoded_data, headers=headers)
        resp.raise_for_status()
        return resp.json()
