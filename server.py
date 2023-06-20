from flask import Flask, redirect, url_for, request
from flask import render_template
from urllib.parse import urlencode
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
    # Example API request - fetch user profile
    profile_response = requests.get('https://api.spotify.com/v1/me', headers={'Authorization': 'Bearer ' + access_token})
    profile_data = profile_response.json()


    # Example API request - fetch user playlists
    playlists_response = requests.get('https://api.spotify.com/v1/me/top/artists', headers={'Authorization': 'Bearer ' + access_token})
    playlists_data = playlists_response.json()
    #print(playlists_data['items'])


    limit = 50
    offset = 0

    while True:
        # Send a GET request to the endpoint with the limit and offset
        params = {
            'market':'US',
            'limit': limit,
            'offset': offset
        }
        response = requests.get('https://api.spotify.com/v1/me/tracks', headers={'Authorization': 'Bearer ' + access_token}, params=params)
        data = response.json()

        # Iterate over each track and display the track name and artists
        for item in data['items']:
            track = item['track']
            track_name = track['name']
            artists = [artist['name'] for artist in track['artists']]

            print(f"Track: {track_name}")
            print(f"Artists: {artists}")
            print()

        # Increment the offset by the limit to get the next page
        offset += limit

        # If there are no more items, exit the loop
        if len(data['items']) < limit:
            break

    topartists = []
    for i in playlists_data['items']:
        ### use a shorter time frame for top artists to get things the user might be more into lately and hasnt seen yet
        ####Create dictionaries and append them to list. You can then sort them using the sorted() function built into python by popularity or 
        ###whatever. ALSO add parameters for length of top artists (time back) and do data scraping basing on all library songs etc. You should also do 
        ### something with the recommendation section of the api. Top songs could also be a good indicator for concert
        topartists.append([i['name'],i['popularity'],i['id']])
        #print(i['name']," - ",i['popularity']," - ",i['id'])
    #print(playlists_response)
    return playlists_data


@app.route("/")
def login():
    params = {
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'scope': 'user-top-read user-library-read',  # Add required scopes
        'redirect_uri': REDIRECT_URI
    }
    auth_url = 'https://accounts.spotify.com/authorize?' + urlencode(params)
    return redirect(auth_url)
