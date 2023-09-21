from flask import Flask, redirect, url_for, request,jsonify, make_response
import collectdata
import fb
from rq import Queue
from redis import Redis


CLIENT_ID = "32f3ca3f815c4b7f91335ffeb5d90f7d"
CLIENT_SECRET = "3f882c04f6824a68b45b251ff922488a"


app = Flask(__name__)

print('spotify loader is running...')

@app.route("/generateData/<spotify_user>/<access_token>",methods=['GET'])
def generateData(spotify_user, access_token):
    #route that accepts spotify user's access token. Endpoint then collects data to be saved for recommendations in the future
    print("Generating data")
    try:
        libdata = collectdata.gatherLibData(access_token)
    except:
        print("Unable to load libdata")
        libdata = None

    try:
        topartists = collectdata.gatherTopArtists(access_token)
    except:
        print("Unable to load topartists")
        topartists = None

    try:
        topsongs = collectdata.gatherTopSongs(access_token)
    except:
        print("Unable to load topsongs")
        topsongs = None

        #add spotify username to this function
    msg,code = fb.addSpotifyData(spotify_user,topartists,libdata,topsongs)

    return make_response({'msg':msg,'status':code})


if __name__ == "__main__":
    app.run(debug=True)