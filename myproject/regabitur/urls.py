from django.conf.urls import url
from django.contrib.auth import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', reg_info, name='reg_info_url'),
]