from flask import Flask, redirect, url_for, request,jsonify, make_response
from flask import render_template
from urllib.parse import urlencode
import collectdata
import main
import base64
import requests
import fb


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
    

    #Using this to test what will go into /generateData
    topartists = collectdata.gatherTopArtists(access_token)
    libdata = collectdata.gatherLibData(access_token)
    
    

    return "test worked"

    '''
    #print(dp.getLibraryData(access_token))
    lst = main.getConcertList(access_token)
    response = make_response(jsonify(lst),201)
    return response '''


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


@app.route("/newUser",methods=['GET'])
def newUser():
    #collect data from request
    email = request.args.get('email')
    first_name = request.args.get('fname')
    last_name = request.args.get('lname')
    max_distance = request.args.get('max_distance')
    location = [request.args.get('location')]

    #attempt to push to db
    try:
        response_msg,response_code = fb.insertUser(email,first_name,last_name,max_distance,location)
        #if response code is 409 (user exists), front end should redirect to login
        return make_response(response_msg,response_code)
    except:
        #return 404 if db system fails
        return make_response({'msg':"Unable to connect to the database"},404)
    

@app.route("/generateData/<email>/<spotify_user>/<access_token>",methods=['GET'])
def generateData(email,spotify_user, access_token):
    #route that accepts spotify user's access token. Endpoint then collects data to be saved for recommendations in the future
    
    
    libdata = collectdata.gatherLibData(access_token)
    topartists = collectdata.gatherTopArtists(access_token)

        #add spotify username to this function
    msg,code = fb.addSpotifyData(email,spotify_user,topartists,libdata)

    return make_response(msg,code)
   
@app.route("/checkUser/<spotify_user>",methods=['GET'])
def checkUser(spotify_user):
    keys = fb.searchDb('spotify_user',spotify_user)
    if keys:
        print('user exists')
        return make_response({'msg':'User exists'},200)
    else:
        print('user does not exists')
        return make_response({'msg':'User does not have an account'},404)