from django.http import HttpResponse


def mainPage(request):
    return HttpResponse('<h1>Hello world</h1>')