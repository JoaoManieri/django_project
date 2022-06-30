from django.shortcuts import render
from django.http import HttpResponse
import datetime

def home(request):
    #now = datetime.datetime.now()
    #html = now;
    #return HttpResponse(html)

    return render(request, 'web_app/home.html')

def sobre(request):
    return render(request, 'web_app/sobre.html')
