from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Parts
from .form import PartsForm

import datetime

def home(request):
    data = {}

    data['now'] = datetime.datetime.now()
    # html = "It is now %s." % now

    return render(request,'service/home.html', data)

def itsWorking(request):
    html = "It's wrking"
    return HttpResponse(html)

def listage(request):
    parameters = {}
    parameters['Parts'] = Parts.objects.all().values()
    return render(request,'service/listage.html', parameters)

def new_parts(request):
    parameters = {}
    form = PartsForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listage')

    parameters['form'] = form
    return render(request, 'service/form.html' ,  parameters)