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
    users.push({
        'email': email,
        'spotify_user': None,
        'fname': fname,
        'lname': lname,
        'maxdist': maxdist,
        'location': location,
        'last_email': None,
        'top_artists': None,
        'lib_artists': None
    })

    result = searchDb('email',email)

    for key in result:
        print(result[key])


def searchDb(search_key,search_value):

    # Retrieve the entire dataset
    all_users = users.get()

    # Filter the data locally based on the key-value pair
    result = {
        key: value
        for key, value in all_users.items()
        if value.get(search_key) == search_value
    }

    return result