from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from .forms import *


# Create your views here.


def reg_info(request):
    """отображает главную страницу приложения regabitur"""
    return render(request, 'regabitur/reg_info.html')


def agreement_flag(request, pk):
    """обработчик соглашения о персональных данных"""
    if (request.user.is_authenticated and request.user.pk==pk):
        if request.method == 'GET':
            abitur = CustomUser.objects.get(user_id=pk)
            abitur.agreement_flag = True
            abitur.save()
    else:
        login_template = 'regabitur/login_abitur.html'
        return render(request, login_template)

    # возвращаемся на предыдущую страницу, используя данные сессии
    request.session['return_path'] = request.META.get('HTTP_REFERER', '/')
    return redirect(request.session['return_path'])


def complete_send(request, pk):
    """Обработчик завершения подачи документов"""
    if (request.user.is_authenticated and request.user.pk==pk):
        if request.method == 'GET':
            abitur = CustomUser.objects.get(user_id=pk)
            abitur.sending_status = 'send'
            abitur.complete_flag = True
            abitur.save()
            print(CustomUser.objects.get(user_id=pk))
    else:
        login_template = 'regabitur/login_abitur.html'
        return render(request, login_template)

    template = 'regabitur/success.html'
    return render(request, template)


class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        """если форма валидна добавляем значение текущего запроса и текущее сообщение (success_msg)"""
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)


class UserRoom(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'regabitur/user_room.html'


    def get_context_data(self, **kwargs):
        """Переопределяем базовый метод, чтобы передать свой контекст"""
        kwargs['dop_info'] = CustomUser.objects.all()
        context = super().get_context_data(**kwargs)
        is_exist = CustomUser.objects.filter(user=self.request.user).exists()
        if is_exist:
            temp = CustomUser.objects.get(user=self.request.user)
            context['status'] = temp.get_sending_status_display()
            context['success'] = temp.sending_status == 'success'
            context['error'] = temp.sending_status == 'error'
            context['agreement'] = temp.agreement_flag == True
            context['is_complete'] = temp.complete_flag == True
        context['is_exist'] = is_exist
        return context


class DocumentsAddView(LoginRequiredMixin, CustomSuccessMessageMixin, CreateView):
    model = DocumentUser
    template_name = 'regabitur/add_doc.html'
    form_class = AddDocForm
    success_url = reverse_lazy('add_doc_url')
    success_msg = 'Документ успешно добавлен!'

    def get_context_data(self, **kwargs):
        """Переопределяем базовый метод, чтобы передать свой контекст"""
        kwargs['documents'] = DocumentUser.objects.all()
        context = super().get_context_data(**kwargs)
        user = CustomUser.objects.get(user=self.request.user)
        user_doc_done = user.complete_flag
        context['user_doc_done'] = user_doc_done
        return context

    def form_valid(self, form):
        """Метод сохранения записи за конкретным пользователем"""
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class InfoCreateView(LoginRequiredMixin, CreateView):
    """Модель для добавления данных в расширенную модель User"""
    model = CustomUser
    template_name = 'regabitur/add_info.html'
    form_class = AddInfoForm
    success_url = reverse_lazy('user_room_url')
    success_msg = 'Данные успешно добавлены!'

    def form_valid(self, form):
        """Метод сохранения записи за конкретным пользователем"""
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class InfoUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'regabitur/add_info.html'
    form_class = AddInfoForm
    success_url = reverse_lazy('user_room_url')
    success_msg = 'Данные успешно обновлены'

    def get_context_data(self, **kwargs):
        """Переопределяем базовый метод, чтобы передать свой контекст"""
        kwargs['update'] = True
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].user:
            return self.handle_no_permission()
        return kwargs


class DocumentDeleteView(LoginRequiredMixin, DeleteView):
    """Класс для удаления документов из таблиц"""
    model = DocumentUser
    template_name = 'regabitur/add_doc.html'
    success_url = reverse_lazy('add_doc_url')
    success_msg = 'Запись удалена'

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)

    def delete(self, request, *args, **kwargs):
        """Переопределяем метод удаления, чтобы запретить удалять чужие записи"""
        # получаем запись объекта из бд
        self.object = self.get_object()
        if self.request.user != self.object.user:
            return self.handle_no_permission()

        success_url = self.get_success_url()

        self.object.delete()
        return HttpResponseRedirect(success_url)


class DocumentsListView(LoginRequiredMixin, ListView):
    """Класс для отображения таблицы с документами пользователей"""
    model = DocumentUser
    template_name = 'regabitur/add_doc.html'
    context_object_name = 'documents'


class MyLoginView(LoginView):
    """обработчик авторизации"""
    template_name = 'regabitur/login_abitur.html'
    form_class = MyLoginForm
    # success_url = reverse_lazy('user_room_url')
    success_url = reverse_lazy('user_room_url')

    def get_success_url(self):
        return self.success_url


class MyRegisterView(CreateView):
    model = User
    template_name = 'regabitur/register_abitur.html'
    form_class = MyRegisterForm
    # success_url = reverse_lazy('user_room_url')
    success_url = reverse_lazy('user_room_url')

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