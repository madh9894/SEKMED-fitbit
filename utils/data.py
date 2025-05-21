import httpx
from datetime import datetime, timedelta
from utils.config import Config

def get_date_range(period):
    """
    Calculate start and end dates based on the requested time period
    
    Args:
        period (str): Time period - 'daily', 'weekly', or 'monthly'
        
    Returns:
        tuple: (start_date, end_date) formatted as YYYY-MM-DD strings
    """
    # Get today's date formatted as YYYY-MM-DD
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Determine start date based on period
    if period == 'daily':
        # For daily, start date is the same as end date
        start_date = today
    elif period == 'weekly':
        # For weekly, start date is 7 days ago
        start_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    elif period == 'monthly':
        # For monthly, start date is 30 days ago
        start_date = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    else:
        # Default to weekly if invalid period provided
        start_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        
    return start_date, today

async def fetch_fitbit_data(access_token, data_type, period='weekly'):
    """
    Fetch data from Fitbit API based on data type and time period
    
    Args:
        access_token (str): Fitbit API access token
        data_type (str): Type of data to fetch ('heart_rate', 'calories', 'steps', 'activity_summary', etc.)
        period (str): Time period - 'daily', 'weekly', or 'monthly'
        
    Returns:
        dict: JSON response from Fitbit API
        
    Raises:
        HTTPException: If the API request fails
    """
    # Set up authorization header
    headers = {"Authorization": f"Bearer {access_token}"}
    
    # Get date range based on requested period
    start_date, end_date = get_date_range(period)
    
    # Construct API URL based on data type
    if data_type == 'heart_rate':
        url = f"{Config.API_BASE_URL}activities/heart/date/{start_date}/{end_date}.json"
    elif data_type == 'calories':
        url = f"{Config.API_BASE_URL}activities/calories/date/{start_date}/{end_date}.json"
    elif data_type == 'steps':
        url = f"{Config.API_BASE_URL}activities/steps/date/{start_date}/{end_date}.json"
    elif data_type == 'distance':
        url = f"{Config.API_BASE_URL}activities/distance/date/{start_date}/{end_date}.json"
    elif data_type == 'activity_summary':
        url = f"{Config.API_BASE_URL}activities/date/{end_date}.json"
    elif data_type == 'sleep':
        url = f"{Config.API_BASE_URL}sleep/date/{start_date}/{end_date}.json"
    else:
        return {"error": "Invalid data type"}
    
    # Make request to Fitbit API
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        return response.json()
