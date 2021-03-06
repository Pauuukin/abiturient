from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import get_object_or_404

from .models import *




def abiturPage(request):
    """возвращаем страницу index и последние 3 новости из базы данных"""
    news = News.objects.all().order_by('-id')[:3]
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


def vstupit_calendar_page(request):
    return render(request, 'abitur/bak/vstupit.html')


def vstupit_calendar_page_mag(request):
    return render(request, 'abitur/mag/vstupit_mag.html')


def bak_calendar(request):
    return render(request, 'abitur/bak/calendar_bak.html')


def mag_calendar(request):
    return render(request, 'abitur/mag/calendar_mag.html')


def mag_page(request):
    return render(request, 'abitur/mag.html')


def infoOVZ_page(request):
    return render(request, 'abitur/infoOVZ.html')


def asp_page(request):
    return render(request, 'abitur/asp.html')


def interPage(request):
    return render(request, 'abitur/inter.html')


def infoPage(request):
    return render(request, 'abitur/info.html')


def spec_bak_1(request):
    return render(request, 'abitur/bak/spec_bak_1.html')


def next_priem(request):
    return render(request, 'abitur/next_priem.html')


def news_list(request):
    news = News.objects.all().order_by('-id')
    return render(request, 'abitur/all_news.html', context={'news': news})


def order_bak(request):
    educational_form = Orders.objects.all().order_by('date_order')
    return render(request, 'abitur/bak/order_bak.html', context={'educational_form': educational_form})


def result_bak(request):
    educational_form = Result.objects.all().order_by('date_result')
    return render(request, 'abitur/bak/result_bak.html', context={'educational_form': educational_form})


def rec_list_bak(request):
    educational_form = RecommendedList.objects.all().order_by('date_order')
    return render(request, 'abitur/bak/rec_list_bak.html', context={'educational_form': educational_form})


def submit_doc_bak(request):
    educational_form = SubmitDoc.objects.all().order_by('date_order')
    return render(request, 'abitur/bak/submit_doc_bak.html', context={'educational_form': educational_form})


def order_mag(request):
    educational_form = OrdersMag.objects.all().order_by('date_order')
    return render(request, 'abitur/mag/order_mag.html', context={'educational_form': educational_form})


def result_mag(request):
    educational_form = ResultMag.objects.all().order_by('date_result')
    return render(request, 'abitur/mag/result_mag.html', context={'educational_form': educational_form})


def rec_list_mag(request):
    educational_form = RecommendedListMag.objects.all().order_by('date_order')
    return render(request, 'abitur/mag/rec_list_mag.html', context={'educational_form': educational_form})


def submit_doc_mag(request):
    educational_form = SubmitDocMag.objects.all()
    return render(request, 'abitur/mag/submit_doc_mag.html', context={'educational_form': educational_form})


def order_asp(request):
    educational_form = OrdersAsp.objects.all().order_by('date_order')
    return render(request, 'abitur/asp/order_asp.html', context={'educational_form': educational_form})


def result_asp(request):
    educational_form = ResultAsp.objects.all().order_by('date_result')
    return render(request, 'abitur/asp/result_asp.html', context={'educational_form': educational_form})


def rec_list_asp(request):
    educational_form = RecommendedListAsp.objects.all().order_by('date_order')
    return render(request, 'abitur/asp/rec_list_asp.html', context={'educational_form': educational_form})


def submit_doc_asp(request):
    educational_form = SubmitDocAsp.objects.all()
    return render(request, 'abitur/asp/submit_doc_asp.html', context={'educational_form': educational_form})









