import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import fb

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {'databaseURL':'https://concertrec-da7fc-default-rtdb.firebaseio.com/'})
ref = db.reference('/py')
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

def addSpotifyData(email,topartists,libdata):
    keys = searchDb('email',email)
    user_key = keys[0]
    user = users.child(user_key)
    user.update({'libdata':libdata,'top_artists':topartists})
    print(user.get())