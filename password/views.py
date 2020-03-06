from django.shortcuts import render

# Create your views here.
from .passwordgen import generate_password

def generatePassword(request):
    # runs generate_password function and saves to a variable which is then passed to 
    # passwordGenerator.html
    password = generate_password()
    return render(request, 'passwordGenerator.html', {'password': password})
