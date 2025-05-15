from flask import Flask, redirect, request, jsonify
from config import Config
from utils.auth import authorize_user, get_token
from utils.data import fetch_fitbit_data
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = Config.SECRET_KEY
app.config.from_object(Config)

CORS(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Fitbit API Backend. Use /authorize to begin."})

@app.route('/authorize', methods=['GET'])
def authorize():
    return redirect(authorize_user())

@app.route('/callback', methods=['GET'])
def callback():
    error = request.args.get('error')
    if error:
        return jsonify({"error": error})

    auth_code = request.args.get('code')
    if not auth_code:
        return jsonify({"error": "Authorization code not found."})

    try:
        tokens = get_token(auth_code)
        access_token = tokens['access_token']
        # redirect to frontend with access token in query param
        return redirect(f"{Config.FRONTEND_URL}/dashboard?token={access_token}")
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/api/data/<data_type>', methods=['GET'])
def get_data(data_type):
    access_token = request.headers.get('Authorization')
    if not access_token:
        return jsonify({"error": "Missing Authorization header"}), 401
    
    if access_token.startswith("Bearer "):
        access_token = access_token.replace("Bearer ", "")

    period = request.args.get('period', '7d')  # default 7 days
    try:
        data = fetch_fitbit_data(access_token, data_type, period)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})

# This is needed for Vercel serverless functions
app.debug = True
