from django.contrib import admin
from pmanager.models import Platform

# Register your models here.
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('platform', 'username', 'password')

admin.site.register(Platform, PlatformAdmin)
