import requests

def fetch_fitbit_data(access_token, data_type, period):
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    valid_types = {
        'steps': 'activities/steps',
        'calories': 'activities/calories',
        'heart': 'activities/heart',
        'distance': 'activities/distance',
        'floors': 'activities/floors',
        'minutesSedentary': 'activities/minutesSedentary',
        'minutesLightlyActive': 'activities/minutesLightlyActive',
        'minutesFairlyActive': 'activities/minutesFairlyActive',
        'minutesVeryActive': 'activities/minutesVeryActive',
    }

    if data_type in valid_types:
        url = f"https://api.fitbit.com/1/user/-/{valid_types[data_type]}/date/today/{period}.json"
    elif data_type == 'sleep':
        url = "https://api.fitbit.com/1.2/user/-/sleep/date/today.json"
    else:
        return {"error": "Unsupported data_type. Use one of: " + ", ".join(valid_types.keys()) + ", sleep"}

    response = requests.get(url, headers=headers)
    
    # Handle expired token or error
    if response.status_code != 200:
        return {"error": f"Fitbit API error: {response.status_code}", "details": response.json()}

    return response.json()
