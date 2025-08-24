from flask import Flask, redirect, request, session, url_for, render_template
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = "SML64536a"

MAX_ARTISTS = 10  # máximo de artistas a mostrar

load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_URL = "https://api.spotify.com/v1/me/top/artists"
SCOPE = "user-top-read"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    auth_url = (
        f"{SPOTIFY_AUTH_URL}?response_type=code&client_id={CLIENT_ID}"
        f"&scope={SCOPE}&redirect_uri={REDIRECT_URI}"
    )
    return redirect(auth_url)

@app.route("/callback")
def callback():
    code = request.args.get("code")
    response = requests.post(
        SPOTIFY_TOKEN_URL,
        data={
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": REDIRECT_URI,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        },
    )
    response_data = response.json()
    session["access_token"] = response_data.get("access_token")
    return redirect(url_for("top_artists"))

@app.route("/top-artists")
def top_artists():
    token = session.get("access_token")
    if not token:
        return redirect(url_for("login"))

    # Obtener time_range desde query string, default medium_term
    time_range = request.args.get("time_range", "medium_term")

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(
        "https://api.spotify.com/v1/me/top/artists",
        headers=headers,
        params={"limit": 10, "time_range": time_range}
    )

    if response.status_code != 200:
        return f"Error: {response.json()}"

    data = response.json()
    artistas = [
        {
            "name": artist["name"],
            "url": artist["external_urls"]["spotify"],
            "image": artist["images"][0]["url"] if artist["images"] else None
        }
        for artist in data["items"]
    ]

    return render_template("top_artists.html", artistas=artistas, selected_range=time_range)
if __name__ == "__main__":
    app.run(debug=True, port=5000)
