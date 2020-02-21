from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(requst):
    return render(requst, 'accounts/login.html')
