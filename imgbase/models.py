from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User)
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    imgur_id = models.CharField(max_length=255)
    
def create_user_cb(sender, instance, **kwargs):
    if created:
        user = User.objects.create()
        instance.user = user
        instance.save()

post_save.connect(create_user_cb, sender=Profile)
