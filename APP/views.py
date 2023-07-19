from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rimpi(request):
    return HttpResponse('<marquee><h1>This is my new project<h1/><marquee/>')
    
