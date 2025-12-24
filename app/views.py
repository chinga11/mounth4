from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def greeting(reequrest):
    return HttpResponse('Home page')