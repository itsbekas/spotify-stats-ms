import os
from flask import Flask, redirect, request, jsonify, session, url_for
from flask_cors import CORS
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import CacheFileHandler
from spotifystats.core.util import check_env

# Check that all required environment variables are set
env_list = [
    "SPOTIPY_CLIENT_ID",
    "SPOTIPY_CLIENT_SECRET",
    "SPOTIPY_REDIRECT_URI"
]

#! DEBUG ONLY
from dotenv import load_dotenv
load_dotenv()

check_env(env_list)

app = Flask(__name__)
CORS(app)

spotify_auth = SpotifyOAuth(
    scope = ["user-read-recently-played"]
)

@app.route("/login")
def login():
    """Redirect user to Spotify login page."""
    auth_url = spotify_auth.get_authorize_url()
    return jsonify(auth_url)

@app.route("/login/callback")
def callback():
    """Callback for Spotify login."""
    code = request.args.get("code")
    token = spotify_auth.get_access_token(code)

    return jsonify(token)

if __name__ == "__main__":
    app.run()
