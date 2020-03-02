from django.urls import path
from .views import generatePassword

urlpatterns = [
    path('generate/', generatePassword, name='platform-generate-page'),
]