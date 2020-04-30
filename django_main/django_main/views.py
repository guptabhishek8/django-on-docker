from django.shortcuts import render
import pyfireconnect
from django.contrib import auth

Config = {
    'apiKey': "AIzaSyCN8RfCVP2gT-MW2ryZTUEAjXVFsw_qqjg",
    'authDomain': "authn-2dd06.firebaseapp.com",
    'databaseURL': "https://authn-2dd06.firebaseio.com",
    'projectId': "authn-2dd06",
    'storageBucket': "authn-2dd06.appspot.com",
    'messagingSenderId': "1078584542869",
    'appId': "1:1078584542869:web:ba520da0ed056ff47d3d9c",
    'measurementId': "G-58S94BH5NE"
}

default_app = pyfireconnect.initialize(Config)

authi = default_app.auth()
databse = default_app.database()


def signin(request):
    return render(request, template_name="signIn.html")


def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get('password')
    try:
        user = authi.sign_in_with_email_and_password(email, passw)
    except:
        message = "invalid credentials"
        return render(request, "signIn.html", {'messa': message})
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    try:
        idtoken = request.session['uid']
        a = authi.get_account_info(idtoken)
        a = a['users']
        a= a[0]
        a = a['localId']
        print("info"+a)
        name = databse.child('users').child(a).child('details').child('name').get().val()
        return render(request, "welcome.html", {'e': name})
    except KeyError:
        message = "User logged out , SignIn again"
        return render(request, "signIn.html", {'messa': message})

def logout(request):
    try:
        del request.session['uid']
    except KeyError:
        pass
    return render(request, 'signIn.html')


def signUp(request):

    return render(request, 'signup.html')


def postsignup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw = request.POST.get('password')
    try:
        user = authi.create_user_with_email_and_password(email, passw)
    except:
        message = "unable to create account try again"
        return render(request, 'signup.html', {"messg": message})

    uid = user['localId']

    data = {"name": name, "status": "1"}
    databse.child("users").child(uid).child("details").set(data)
    return render(request, "signIn.html")
