import os

from rauth import OAuth2Service

ImgurAuth = OAuth2Service(
    client_id=os.environ['IMGUR_CLIENT_ID'],
    client_secret=os.environ['IMGUR_CLIENT_SECRET'],
    name='imgfav',
    authorize_url='https://api.imgur.com/oauth2/authorize',
    access_token_url='https://api.imgur.com/oauth2/token',
    base_url='https://api.imgur.com')


