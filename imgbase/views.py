from django.shortcuts import render, redirect

from .auth import ImgurAuth

def home(request):
    print(ImgurAuth.access_token)
    render(request, 'home.html')

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
    
    if not code:
        return redirect('/')
    
    redirect_uri = 'http://localhost:8000/auth/granted'
    session = ImgurAuth.get_auth_session(data={
        'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': redirect_uri
    })
    
    return redirect('/')

