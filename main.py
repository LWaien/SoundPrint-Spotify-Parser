from flask import Flask, redirect, url_for, request,jsonify, make_response
import collectdata
import fb
import os
from rq import Queue
from redis import Redis


CLIENT_ID = "32f3ca3f815c4b7f91335ffeb5d90f7d"
CLIENT_SECRET = "3f882c04f6824a68b45b251ff922488a"


redis_conn = Redis.from_url(os.getenv('REDIS_URL'))
queue = Queue('my_queue', connection=redis_conn)

app = Flask(__name__)

print('spotify loader is running...')

@app.route("/generateData/<spotify_user>/<access_token>",methods=['GET'])
def generateData(spotify_user, access_token):
    #route that accepts spotify user's access token. Endpoint then collects data to be saved for recommendations in the future
    print("Generating data")
    try:
        #libdata = collectdata.gatherLibData(access_token)
        print("loading user libdata")
        libdata = queue.enqueue(collectdata.gatherLibData, access_token)
    except:
        print("Unable to load libdata")
        libdata = None

    try:
        #topartists = collectdata.gatherTopArtists(access_token)
        print("loading user topartists")
        topartists = queue.enqueue(collectdata.gatherTopArtists, access_token)
    except:
        print("Unable to load topartists")
        topartists = None

    try:
        #topsongs = collectdata.gatherTopSongs(access_token)
        print("loading user top songs")
        topsongs = queue.enqueue(collectdata.gatherTopSongs, access_token)
    except:
        print("Unable to load topsongs")
        topsongs = None

        #add spotify username to this function
    #msg,code = fb.addSpotifyData(spotify_user,topartists.result,libdata.result,topsongs.result)
    print("Adding spotify data")
    add = queue.enqueue(fb.addSpotifyData, spotify_user,topartists.result,libdata.result,topsongs.result)
    print("Spotify data added")
    return make_response({'msg':'adding data','status':200})


if __name__ == "__main__":
    app.run(debug=True)