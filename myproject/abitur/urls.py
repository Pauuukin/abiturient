from django.urls import path

from .views import *

urlpatterns = [
    path('', abiturPage),
    path('bak/', bakPage)
]