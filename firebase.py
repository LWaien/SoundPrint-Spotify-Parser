import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json


#users.push({'Name':'Logan','Email':'blah blah blah'})
#users.child('OtherName').set({'Name':'Logan','Email':'blah blah blah'})
#print(users.child('OthrName').get())

def insertUser(email,fname,lname,maxdist,location):
    cred = credentials.Certificate("credentials.json")
    firebase_admin.initialize_app(cred, {'databaseURL':'https://concertrec-da7fc-default-rtdb.firebaseio.com/'})
    ref = db.reference('/py')
    users = ref.child('users')
    users.push({'email':email,'spotify_user':None,'fname':fname,'lname':lname,'maxdist':maxdist,'location':location,
                           'last_email':None,'top_artists':None, 'lib_artists':None})