from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Password(models.Model):
    platform = models.CharField(max_length=20)
    username = models.CharField(max_length=settings.PMANAGER_USERNAME_MAX_LENGTH)
    password = models.CharField(max_length=30)
