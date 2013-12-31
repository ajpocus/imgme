import os
import cgi

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

import oauth2

from .auth import ImgurAuth

consumer = oauth2.Consumer(os.environ['IMGUR_CLIENT_ID'],
    os.environ['IMGUR_CLIENT_SECRET'])
client = oauth2.Client(consumer)
base_url = "https://api.imgur.com"
authorize_url = base_url + "/oauth2/authorize"
token_url = base_url + "/oauth2/token"
redirect_url = "http://localhost:8000/auth/granted"

def home(request):
    print(ImgurAuth.access_token)
    render(request, 'home.html')

def auth(request):
    resp, content = client.request(authorize_url, "GET")
    if resp['status'] != '200':
        raise Exception("Invalid response from Twitter.")

    request.session['request_token'] = dict(cgi.parse_qsl(content))
    url = "%s?oauth_token=%s" % (token_url,
        request.session['request_token']['oauth_token'])
    return redirect(url)
    
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

