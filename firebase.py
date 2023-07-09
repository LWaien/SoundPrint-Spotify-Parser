import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json


#users.push({'Name':'Logan','Email':'blah blah blah'})
#users.child('OtherName').set({'Name':'Logan','Email':'blah blah blah'})
#print(users.child('OthrName').get())

def insertUser(email,fname,lname,maxdist,location):
    print('db')
    cred = credentials.Certificate("credentials.json")
    print('cred')
    firebase_admin.initialize_app(cred, {'databaseURL':'https://concertrec-da7fc-default-rtdb.firebaseio.com/'})
    print('init')
    ref = db.reference('/py')
    print('ref')
    users = ref.child('users')
    print('ref2')
    users.child(email).set({'spotify_user':None,'fname':fname,'lname':lname,'maxdist':maxdist,'location':location,
                            'last_email':None,'top_artists':None, 'lib_artists':None})
    print('added to db')