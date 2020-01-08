# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):

    message = "Hello Diadji"

    return HttpResponse(message)

def listing(request):
    if request.method == 'POST':
        chaine = request.POST['tele']
        series = [x.encode('UTF8') for x in request.POST['list-series']]
        print(chaine)
        print(series)
    return render(request, 'store/templates/index.html')
