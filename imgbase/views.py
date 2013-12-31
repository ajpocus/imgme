from django.shortcuts import render, redirect

from .auth import ImgurAuth

def auth(request):
    redirect_uri = 'http://localhost:8000/auth/granted'
    params = {
        'scope': '',
        'response_type': 'code',
        'redirect_uri': redirect_uri
    }
    
    url = ImgurAuth.get_authorize_url(**params)
    return redirect(url)
    
def granted(request):
    code = request.GET['code']
    print(code)
    redirect_uri = 'http://localhost:8000/auth/granted'
    session = ImgurAuth.get_auth_session(data={
        'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': redirect_uri
    })
    
    print(session)
