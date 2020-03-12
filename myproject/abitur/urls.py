from django.urls import path

from .views import *

urlpatterns = [
    path('', abiturPage),
    path('bak/', bakPage),
    path('inter/', interPage),
    path('info/', infoPage),
    path('bak/spec_bak_1', spec_bak_1)
]