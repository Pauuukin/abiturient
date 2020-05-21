from django.shortcuts import render

# Create your views here.


def reg_info(request):
    return render(request, 'regabitur/reg_info.html')