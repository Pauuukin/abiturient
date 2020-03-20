from django.urls import path

from .views import *

urlpatterns = [
    path('', abiturPage),
    path('news/<str:slug>/', NewsDetail.as_view(), name='news_detail_url'),
    path('bak/', bakPage, name='bakPage_url'),
    path('inter/', interPage, name='interPage_url'),
    path('info/', infoPage, name='infoPage_url'),
    path('bak/spec_bak_1/', spec_bak_1, name='spec_bak_1_url'),
    path('spec_bak_1/', spec_bak_1, name='spec_bak_1_url'),
    path('news/', news_list, name='news_list_url'),
    path('bak/order_bak/', order_bak, name='order_bak_url'),
    path('bak/rec_list_bak/', rec_list_bak, name='rec_list_bak_url'),
    path('bak/submit_doc_bak/', submit_doc_bak, name='submit_doc_bak_url')
]