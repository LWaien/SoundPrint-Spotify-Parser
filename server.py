from flask import Flask, redirect, url_for, request
from flask import render_template
from urllib.parse import urlencode
import main
import dataParser as dp
import base64
import requests


CLIENT_ID = "32f3ca3f815c4b7f91335ffeb5d90f7d"
CLIENT_SECRET = "3f882c04f6824a68b45b251ff922488a"
REDIRECT_URI = "http://127.0.0.1:5000/redirect"


app = Flask(__name__)

@app.route("/redirect")
def formdisplay():
    auth_code = request.args.get('code')

    # Exchange the authorization code for an access token
    headers = {
        'Authorization': 'Basic ' + base64.b64encode(f'{CLIENT_ID}:{CLIENT_SECRET}'.encode()).decode(),
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'authorization_code',
        'code': auth_code,
        'redirect_uri': REDIRECT_URI
    }
    response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=urlencode(data))
    token_data = response.json()
    # Use the access token to make API requests on behalf of the user
    access_token = token_data.get('access_token')
    

    #print(dp.getLibraryData(access_token))
    topartists = [artist['artist_id'] for artist in dp.getTopArtists(access_token)]
    lst = main.getConcertList(topartists)
    #remove blank entries and then split by within a month of now and try to pick 5-10 of those first. Save anything father out for next month
    final_top_artists = []
    for artist in lst:
        if artist:
            final_top_artists.append(artist)
    print(final_top_artists)
    return "hello"


@app.route("/")
def login():
    print('running')
    params = {
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'scope': 'user-top-read user-library-read',  # Add required scopes
        'redirect_uri': REDIRECT_URI
    }
    auth_url = 'https://accounts.spotify.com/authorize?' + urlencode(params)
    return redirect(auth_url)
