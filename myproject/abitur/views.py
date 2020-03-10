from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def abiturPage(request):
    news = News.objects.all()
    return render(request, 'abitur/index.html', context={'news': news})

def bakPage(request):
    return render(request, 'abitur/bak.html')

def interPage(request):
    return render(request, 'abitur/inter.html')