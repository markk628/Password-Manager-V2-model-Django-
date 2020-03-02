from django.shortcuts import render

# Create your views here.
from .passwordgen import generate_password

def generatePassword(request):
    password = generate_password()
    return render(request, 'passwordGenerator.html', {'password': password})
