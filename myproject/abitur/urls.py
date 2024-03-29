from django.urls import path

from .views import *

urlpatterns = [
    path('', abiturPage, name='main_abitur_url'),
    path('submit/', submitPage, name='submit_url'),
    path('rec/', recommended_page, name='recommended_url'),
    path('news/<str:slug>/', NewsDetail.as_view(), name='news_detail_url'),
    path('bak/', bakPage, name='bakPage_url'),
    path('bak/vstupit_calendar_page/', vstupit_calendar_page, name='vstupit_calendar_page_url'),
    path('spec/vstupit_calendar_page/', vstupit_calendar_page_spec, name='vstupit_calendar_page_spec_url'),
    path('mag/vstupit_mag/', vstupit_calendar_page_mag, name='vstupit_calendar_page_mag_url'),
    path('inter/', interPage, name='interPage_url'),
    path('next_priem/', next_priem, name='next_priem_url'),
    path('info/', infoPage, name='infoPage_url'),
    path('bak/spec_bak_1/', spec_bak_1, name='spec_bak_1_url'),
    path('spec_bak_1/', spec_bak_1, name='spec_bak_1_url'),
    path('news/', news_list, name='news_list_url'),
    path('bak/order_bak/', order_bak, name='order_bak_url'),
    path('bak/rec_list_bak/', rec_list_bak, name='rec_list_bak_url'),
    path('mag/order_mag/', order_mag, name='order_mag_url'),
    path('mag/rec_list_mag/', rec_list_mag, name='rec_list_mag_url'),
    path('asp/order_asp/', order_asp, name='order_asp_url'),
    path('asp/rec_list_asp/', rec_list_asp, name='rec_list_asp_url'),
    path('mag/', mag_page, name='mag_page_url'),
    path('asp/', asp_page, name='asp_page_url'),
    path('spec/', spec_page, name='spec_page_url'),
    path('normative-doc/', norm_doc, name='norm_doc_page_url'),
    # path('infoOVZ/', infoOVZ_page, name='infoOVZ_page_url'),
    path('bak/calendar/', bak_calendar, name='bak_calendar_url'),
    path('spec/calendar/', spec_calendar, name='spec_calendar_url'),
    path('mag/calendar/', mag_calendar, name='mag_calendar_url'),
    path('bak/result_bak/', result_bak, name='result_bak_url'),
    path('mag/result_mag/', result_mag, name='result_mag_url'),
    path('asp/result_asp/', result_asp, name='result_asp_url')
]