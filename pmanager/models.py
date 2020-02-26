from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Platform(models.Model):
    platform = models.CharField(max_length=20)
    username = models.CharField(max_length=settings.PMANAGER_USERNAME_MAX_LENGTH)
    password = models.CharField(max_length=30)
    slug = models.CharField(max_length=settings.PMANAGER_USERNAME_MAX_LENGTH, blank=True, editable=False)

    def __str__(self):
        return self.platform

    def get_url(self):
        path_components = {'slug': self.slug}
        return reverse('pm-platform-page', kwargs=path_components)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.platform, allow_unicode=True)

        return super(Platform, self).save(*args, **kwargs)