from flask import Flask, redirect, url_for, request,jsonify, make_response
import collectdata
import fb


CLIENT_ID = "32f3ca3f815c4b7f91335ffeb5d90f7d"
CLIENT_SECRET = "3f882c04f6824a68b45b251ff922488a"


app = Flask(__name__)

@app.route("/generateData/<spotify_user>/<access_token>",methods=['GET'])
def generateData(spotify_user, access_token):
    #route that accepts spotify user's access token. Endpoint then collects data to be saved for recommendations in the future
    print("genData")

    libdata = collectdata.gatherLibData(access_token)
    topartists = collectdata.gatherTopArtists(access_token)
    topsongs = collectdata.gatherTopSongs(access_token)

        #add spotify username to this function
    msg,code = fb.addSpotifyData(spotify_user,topartists,libdata,topsongs)

    return make_response({'msg':msg,'status':code})

