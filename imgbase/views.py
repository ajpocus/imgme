import os
import cgi

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from requests_oauthlib import OAuth2Session

from .auth import ImgurAuth

client_id = os.environ['IMGUR_CLIENT_ID']
client_secret = os.environ['IMGUR_CLIENT_SECRET']
base_url = "https://api.imgur.com"
authorize_url = base_url + "/oauth2/authorize"
token_url = base_url + "/oauth2/token"
redirect_uri = "http://localhost:8000/auth/granted"

def home(request):
    print(ImgurAuth.access_token)
    render(request, 'home.html')

def auth(request):
    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)
    redirect_url, state = oauth.authorization_url(authorize_url)
        
    return redirect(redirect_url)
    
def granted(request):
    code = request.GET['code']

    if not code:
        return redirect('/')
    print(request)
    redirect_uri = 'http://localhost:8000/auth/granted'
    session = ImgurAuth.get_auth_session(data={
        'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': redirect_uri
    })
    print(session)
    
    return redirect('/')

