from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User)
    oauth_token = models.CharField(max_length=255)
    oauth_secret = models.CharField(max_length=255)

