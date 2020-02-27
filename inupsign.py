import pyrebase
import json

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


def getupuser(el, pword, name):
    print("making user")
    try:
        user = auth.create_user_with_email_and_password(el, pword)
        uid = user['localId']
        try:
            print (uid)
            firedb.child("Users").child(uid).update({"id": el, "password": pword, "name": name})
            p_data = {
                "id": el,
                "password": pword
            }
            with open('data.json', 'w') as json_file:
                json.dump(p_data, json_file)
            print ("Made you New User")
            return name
        except:
            print("Unexpected Error")
            return False
    except:
        print("User Already Exsists")
        return False



def getinuser(el, pword):
    print("signing user")

    try:
        user = auth.sign_in_with_email_and_password(el, pword)
        uid = user['localId']
        print (uid)
        try:
            print (el)
            firedb.child("Users").child(uid).update({"id": el, "password": pword})
            p_data = {
                "id": el,
                "password": pword
            }
            with open('data.json', 'w') as json_file:
                json.dump(p_data, json_file)

            data =  firedb.child("Users").child(uid).child("name").get()
            return data.val()
        except:
            print("Unexpected Error")
            return False
    except:
        print("Please Enter Correct Credentials")
        return False