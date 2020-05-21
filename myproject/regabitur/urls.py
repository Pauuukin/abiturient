from django.conf.urls import url
from django.contrib.auth import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', reg_info, name='reg_info_url'),
    path('accounts/login/', MyLoginView.as_view(), name='login_abitur_url'),
    path('login/', MyLoginView.as_view(), name='login_abitur_url'),
    path('register-abitur/', MyRegisterView.as_view(), name='register_abitur_url'),
    path('logout-abitur', MyLogoutView.as_view(), name='logout_abitur_url'),
    url(r'^password-reset/$', views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^password-reset/done/$', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',  views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^password-reset/complete/$', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]