from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import get_object_or_404

from .models import *

# Create your views here.

def abiturPage(request):
    news = News.objects.all()
    return render(request, 'abitur/index.html', context={'news': news})

# def news_detail(request, slug):
#        """view обрабатывается функцией"""
#      news = News.objects.get(slug__iexact=slug)
#      return render(request, 'abitur/news_detail.html', context={'news' : news})

class NewsDetail(View):
    """теперь view обрабатывается классом"""
    def get(self, request, slug):
         # news = News.objects.get(slug__iexact=slug)
        news = get_object_or_404(News, slug__iexact=slug)
        return render(request, 'abitur/news_detail.html', context={'news': news})

def bakPage(request):
    return render(request, 'abitur/bak.html')

def interPage(request):
    return render(request, 'abitur/inter.html')

def infoPage(request):
    return render(request, 'abitur/info.html')

def spec_bak_1(request):
    return render(request, 'abitur/bak/spec_bak_1.html')

def news_list(request):
    news = News.objects.all()
    return render(request, 'abitur/all_news.html', context={'news': news})