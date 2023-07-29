import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import fb

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {'databaseURL':'https://concertrec-da7fc-default-rtdb.firebaseio.com/'})
ref = db.reference()
users = ref.child('users')

def insertUser(email,fname,lname,maxdist,location):
    exists = searchDb('email',email)

    if exists:
        return {'msg':'user already exists'},409
    else:
        users.push({
            'email': email,
            'spotify_user': '',
            'fname': fname,
            'lname': lname,
            'maxdist': maxdist,
            'location': location,
            'last_email': '',
            'top_artists': '',
            'libdata': ''
        })

        return {'msg':'user was successfully added to the the database'},201

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

def addSpotifyData(email,spotify_user,topartists,libdata):
    #search for user in db
    keys = searchDb('email',email)

    if keys is None:
        return {'msg':'Could Not Find User'},404
    
    #returns list of ids for applicable entries
    user_key = keys[0]
    #referencing the user we want to add data for
    user = users.child(user_key)
    user.update({'spotify_user':spotify_user,'libdata':libdata,'top_artists':topartists})
    #print(user.get())
    return 'Library Data Added!',201

def checkData(spotify_user):
    keys = searchDb('spotify_user',spotify_user)
    user = users.child(keys[0])

    if user.get('libdata') is None and user.get('top_artists') is None:
        #return false as in user data does not exist
        return False
    else:
        return True

def getEmail(spotify_user):
    keys = searchDb('spotify_user',spotify_user)
    print(keys[0])
    user = users.child(keys[0])

    return user.get('email')