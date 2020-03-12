from django.urls import path

from .views import *

urlpatterns = [
    path('', abiturPage),
    path('news/<str:slug>/', news_detail, name='news_detail_url'),
    path('bak/', bakPage, name='bakPage_url'),
    path('inter/', interPage, name='interPage_url'),
    path('info/', infoPage, name='infoPage_url'),
    path('bak/spec_bak_1/', spec_bak_1, name='spec_bak_1_url'),
    path('spec_bak_1/', spec_bak_1, name='spec_bak_1_url')
]