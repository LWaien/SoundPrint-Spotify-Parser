from flask import Flask, redirect, url_for, request,jsonify, make_response
import collectdata
import fb
import threading
from flask_cors import CORS


CLIENT_ID = "32f3ca3f815c4b7f91335ffeb5d90f7d"
CLIENT_SECRET = "3f882c04f6824a68b45b251ff922488a"


app = Flask(__name__)
CORS(app)  

print('spotify loader is running...')

#global variables to track loading process
loadingFlag = False
progress = 0
lock1 = threading.Lock()
lock2 = threading.Lock()

@app.route("/generateData/<spotify_user>/<access_token>",methods=['GET'])
def generateData(spotify_user, access_token):
    #route that accepts spotify user's access token. Endpoint then collects data to be saved for recommendations in the future
    print("Generating data")
    
    thread = threading.Thread(target=scanSpotify, args=(spotify_user, access_token))
    thread.start()

    return make_response({'msg':'scanning spotify','status':200})


def scanSpotify(spotify_user,access_token):
    loading = True

    try:
        print("loading libdata")
        libdata = collectdata.gatherLibData(access_token)
    except:
        print("Unable to load libdata")
        libdata = None

    try:
        print("loading topartists")
        topartists = collectdata.gatherTopArtists(access_token)
    except:
        print("Unable to load topartists")
        topartists = None

    try:
        print("loading topsongs")
        topsongs = collectdata.gatherTopSongs(access_token)
    except:
        print("Unable to load topsongs")
        topsongs = None

        #add spotify username to this function
    msg,code = fb.addSpotifyData(spotify_user,topartists,libdata,topsongs)
    #print(code)+
    loading = False

@app.route("/getProgress",methods=['GET'])
def getProgress():
    lock1.acquire()
    global progress
    prog = progress
    lock2.release()
    return jsonify({'progress': prog})
    
        
        

def updateProgress(update_val):
    lock2.acquire()
    global progress
    progress = update_val
    lock1.release()

    

if __name__ == "__main__":
    app.run(debug=True)