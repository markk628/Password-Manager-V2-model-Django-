from django.conf import settings
from django.db import models


# Create your models here.
class Platform(models.Model):
    # users can enter the platform name, username, and password
    platform = models.CharField(max_length=20)
    username = models.CharField(max_length=settings.PMANAGER_USERNAME_MAX_LENGTH)
    password = models.CharField(max_length=30)

    

