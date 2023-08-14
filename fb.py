import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import fb

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {'databaseURL':'https://concertrec-da7fc-default-rtdb.firebaseio.com/'})
ref = db.reference()
users = ref.child('users')

def insertEmailInfo(spotify_user, email,fname,lname,maxdist,location):
    keys = searchDb('spotify_user',spotify_user)
    user_key = keys[0]
    #referencing the user we want to add data for
    user = users.child(user_key)
    
    user.push({
        'email': email,
        'fname': fname,
        'lname': lname,
        'maxdist': maxdist,
        'location': location,
        
        })

    return {'msg':'email info successfully added to the the database'},201

def createNewUser(spotify_user):
    users.push({
        'email': '',
        'spotify_user': spotify_user,
        'fname': '',
        'lname': '',
        'maxdist': '',
        'location': '',
        'last_email': '',
        'top_artists': '',
        'libdata': ''
        })


def searchDb(search_key,search_value):

    # Retrieve the entire dataset
    user = users.get()

    # Filter the data locally based on the key-value pair
    if user:
        result = {
            key: value
            for key, value in user.items()
            if value.get(search_key) == search_value
        }
        key_ids = list(result.keys())
        return key_ids
    else:
        return None

def addSpotifyData(spotify_user,topartists,libdata):
    #search for user in db
    print(f"Adding user data for {spotify_user}")
    keys = searchDb('spotify_user',spotify_user)

    if keys is None:
        return {'msg':'Could Not Find User'},404
    
    #returns list of ids for applicable entries
    user_key = keys[0]
    #referencing the user we want to add data for
    user = users.child(user_key)
    user.update({'libdata':libdata,'top_artists':topartists})
    #print(user.get())
    return 'Library data added',201

def checkData(spotify_user):
    keys = searchDb('spotify_user',spotify_user)
    user = users.child(keys[0])

    if user.get('libdata') is None and user.get('top_artists') is None:
        #return false as in user data does not exist
        return False
    else:
        return True
