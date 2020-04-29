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
    path('bak/submit_doc_bak/', submit_doc_bak, name='submit_doc_bak_url'),
    path('mag/order_mag/', order_mag, name='order_mag_url'),
    path('mag/rec_list_mag/', rec_list_mag, name='rec_list_mag_url'),
    path('mag/submit_doc_mag/', submit_doc_mag, name='submit_doc_mag_url'),
    path('asp/order_asp/', order_asp, name='order_asp_url'),
    path('asp/rec_list_asp/', rec_list_asp, name='rec_list_asp_url'),
    path('asp/submit_doc_asp/', submit_doc_asp, name='submit_doc_asp_url'),
    path('mag/', mag_page, name='mag_page_url'),
    path('asp/', asp_page, name='asp_page_url'),
    path('infoOVZ/', infoOVZ_page, name='infoOVZ_page_url'),
    path('bak/calendar/', bak_calendar, name='bak_calendar_url'),
    path('bak/result_bak/', result_bak, name='result_bak_url'),
    path('mag/result_mag/', result_mag, name='result_mag_url'),
    path('asp/result_asp/', result_asp, name='result_asp_url')
]