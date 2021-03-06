import os
import cgi
import json

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from requests_oauthlib import OAuth2Session

from .models import Profile

client_id = os.environ['IMGUR_CLIENT_ID']
client_secret = os.environ['IMGUR_CLIENT_SECRET']
base_url = "https://api.imgur.com"
authorize_url = base_url + "/oauth2/authorize"
token_url = base_url + "/oauth2/token"
redirect_uri = "http://localhost:8000/auth/granted"

oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)

def home(request):
    return render(request, 'home.html')

def auth(request):
    redirect_url, state = oauth.authorization_url(authorize_url)
        
    return redirect(redirect_url)
    
def granted(request):
    code = request.GET['code']
    secret = os.environ['IMGUR_CLIENT_SECRET']
    token = oauth.fetch_token(token_url, code=code, client_secret=secret)
    
    res = oauth.get(base_url + "/3/account/me")
    obj = json.loads(res.text)
    me = obj['data']
    
    print(me)
    
    profile = Profile.objects.get(imgur_id=me['id'])
    if not profile:
        profile = Profile.objects.create(me)
        login(request, profile.user)
        
    print (r.text)
    print(token)
    
    return redirect("/")
    
