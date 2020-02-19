from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def abiturPage(request):
    n = ['Oleg', 'igor', 'inna', 'artem', 'nastya']
    return render(request, 'abitur/index.html', context={'names': n})

def bakPage(request):
    return HttpResponse('<h1>Bak page</h1>')