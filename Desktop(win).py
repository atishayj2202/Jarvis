import pyrebase
import json
import os.path
from os import path
from GUI_desktop import create_UI

Config = {
    "apiKey": "AIzaSyCiLDPLNA6POpKQgTxTP9NoQCqx7-am2Ls",
    "authDomain": "jarvis-2202-983f9.firebaseapp.com",
    "databaseURL": "https://jarvis-2202-983f9.firebaseio.com",
    "projectId": "jarvis-2202-983f9",
    "storageBucket": "jarvis-2202-983f9.appspot.com",
    "messagingSenderId": "106957765273",
    "appId": "1:106957765273:web:62678a9ead36c8f0f29608",
    "measurementId": "G-5GXSB61Q70"
}

firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
firedb = firebase.database()
global uid

def main_D():
    if path.exists("data.json"):

        with open('data.json') as f:
            data = json.load(f)
        pword = data["password"]
        el = data["id"]
        try:
            auth.sign_in_with_email_and_password(el, pword)
        except:
            os.remove("data.json")
            create_UI()
    else:
        print ("path do not exsist")
        create_UI()

main_D()
# try:
# data = firedb.child("Users").child("monikaj2202").child("id").get()
# print (data.val())
# firedb.child("Users").child(pword).update({"id" : el})
#   user = auth.sign_in_with_email_and_password(el,pword)
#    print("Success")
# except:
# print("Error")
