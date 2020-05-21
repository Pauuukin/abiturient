from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, login

from .forms import *


# Create your views here.


def reg_info(request):
    """отображает главную страницу приложения regabitur"""
    return render(request, 'regabitur/reg_info.html')


class MyLoginView(LoginView):
    """обработчик авторизации"""
    template_name = 'regabitur/login_abitur.html'
    form_class = MyLoginForm
    # success_url = reverse_lazy('user_room_url')
    success_url = reverse_lazy('reg_info_url')

    def get_success_url(self):
        return self.success_url


class MyRegisterView(CreateView):
    model = User
    template_name = 'regabitur/register_abitur.html'
    form_class = MyRegisterForm
    # success_url = reverse_lazy('user_room_url')
    success_url = reverse_lazy('reg_info_url')

    def form_valid(self, form):
        """если пользователь зарегистрировался, сразу входим в систему"""
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        auth_user = authenticate(username=username, password=password)
        login(self.request, auth_user)
        return form_valid


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('reg_info_url')