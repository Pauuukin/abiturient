from os.path import exists

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import View, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from .forms import *

# Create your views here.
from .models import PublishTab


class MainPageView(TemplateView):
    template_name = 'regabitur/reg_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['custom_exist'] = hasattr(user, 'custom')
        context['addition_exist'] = hasattr(user, 'addition')
        return context

# def reg_info(request):
#     """отображает главную страницу приложения regabitur"""
#     return render(request, 'regabitur/reg_info.html')


def agreement_flag(request, pk):
    """обработчик соглашения о персональных данных"""
    if request.user.is_authenticated and request.user.pk == pk:
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
    if (request.user.is_authenticated and request.user.pk == pk):
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
    """Миксин для вывода сообщений при работе с формами"""

    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        """если форма валидна добавляем значение текущего запроса и текущее сообщение (success_msg)"""
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)


"""
    Личный кабинет пользователя
"""


class UserRoom(LoginRequiredMixin, ListView):
    """Личный кабинет пользователя"""
    model = CustomUser
    template_name = 'regabitur/user_room.html'

    def get_context_data(self, **kwargs):
        """Переопределяем базовый метод, чтобы передать свой контекст"""
        user = self.request.user
        custom_user = CustomUser.objects.get(user=user.id)
        profile = AdditionalInfo.objects.get(user=user.id)
        context = super().get_context_data(**kwargs)
        context['user'] = CustomUser.objects.get(user=user.id)
        context['profile'] = profile.education_profile.all() # выводим информацию из ManyToMany related
        context['number'] = user.publish.individual_str
        context['status'] = custom_user.get_sending_status_display()
        context['success'] = custom_user.sending_status == 'success'
        context['error'] = custom_user.sending_status == 'error'
        context['agreement'] = custom_user.agreement_flag
        context['is_complete'] = custom_user.complete_flag
        context['custom_exist'] = hasattr(user, 'custom')
        context['addition_exist'] = hasattr(user, 'addition')
        return context


# def get_template_names(self):
#     user = self.request.user
#     custom_exist = hasattr(user, 'custom')
#     addition_exist = hasattr(user, 'addition')
#     if custom_exist and addition_exist:
#         self.template_name = 'regabitur/user_room.html'
#     elif custom_exist:
#         self.template_name = 'regabitur/reg_info.html'
#     else:
#         self.template_name = 'regabitur/reg_info.html'
#     return self.template_name


"""
    Добавляем доп. данные  
"""


class InfoCreateView(LoginRequiredMixin, CreateView):
    """Модель для добавления данных в расширенную модель User"""
    model = CustomUser
    template_name = 'regabitur/add_info.html'
    form_class = AddInfoForm
    success_url = reverse_lazy('add_additional_url')
    success_msg = 'Данные успешно добавлены!'

    def form_valid(self, form):
        """Метод сохранения записи за конкретным пользователем"""
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class InfoUpdateView(LoginRequiredMixin, UpdateView):
    """Класс обновления информации"""
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


"""
    Выбираем формы обучения 
"""


class AdditionalInfoView(LoginRequiredMixin, CreateView):
    """Класс для выбора профиля обучения"""
    model = AdditionalInfo
    template_name = 'regabitur/add_profile.html'
    form_class = AdditionalInfoForm
    success_url = reverse_lazy('user_room_url')

    def form_valid(self, form):
        """Метод сохранения записи за конкретным пользователем"""
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


"""
    CRUD для документов
"""


class DocumentsAddView(LoginRequiredMixin, CustomSuccessMessageMixin, CreateView):
    model = DocumentUser
    template_name = 'regabitur/add_doc.html'
    form_class = AddDocForm
    success_url = reverse_lazy('add_doc_url')
    success_msg = 'Документ успешно добавлен!'

    def get_context_data(self, **kwargs):
        """Переопределяем базовый метод, чтобы передать свой контекст"""
        context = super().get_context_data(**kwargs)
        id_user = self.request.user
        user = CustomUser.objects.get(user=id_user)
        document_user = DocumentUser.objects.filter(user=id_user)
        user_doc_done = user.complete_flag
        context['user_doc_done'] = user_doc_done
        context['document_user'] = document_user
        context['custom_exist'] = hasattr(id_user, 'custom')
        context['addition_exist'] = hasattr(id_user, 'addition')
        return context

    def form_valid(self, form):
        """Метод сохранения записи за конкретным пользователем"""
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


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


"""
     Классы регистрации и авторизации пользователей
"""


class MyLoginView(LoginView):
    """обработчик авторизации"""
    template_name = 'regabitur/login_abitur.html'
    form_class = MyLoginForm

    # success_url = reverse_lazy('user_room_url')

    def get_success_url(self):
        """
        Определяем, есть ли связанные модели для дополнительной информации(CustomUser, AdditionalUser)|
        Если нет, отправляем на страницу с добавлением недостающей информации
        """
        user = self.request.user
        custom_exist = hasattr(user, 'custom')
        addition_exist = hasattr(user, 'addition')
        if custom_exist and addition_exist:
            self.success_url = reverse_lazy('user_room_url')
        elif custom_exist:
            self.success_url = reverse_lazy('add_additional_url')
        else:
            self.success_url = reverse_lazy('add_info_url')
        return self.success_url


class MyRegisterView(CreateView):
    """Регистрация пользователя"""
    model = User
    template_name = 'regabitur/register_abitur.html'
    form_class = MyRegisterForm
    success_url = reverse_lazy('add_info_url')

    def form_valid(self, form):
        """если пользователь зарегистрировался, сразу входим в систему"""
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        auth_user = authenticate(username=username, password=password)
        login(self.request, auth_user)
        return form_valid


class MyLogoutView(LogoutView):
    """ВЫход из системы """
    next_page = reverse_lazy('reg_info_url')


"""
    Списки подавших документы
"""

"""
    Бакалавриат
"""

class BacOfoGp(ListView):
    """БАК ОФО ГП"""
    model = PublishTab
    template_name = 'regabitur/submit/bak_ofo_gp.html'

    def get_context_data(self, **kwargs):
        """Передаем записи с БАК ОФО true """
        context = super().get_context_data(**kwargs)
        all_publish = PublishTab.objects.filter(bak_ofo_gp=True)
        context["list"] = all_publish
        return context


class BacOfoUp(ListView):
    """БАК ОФО УП"""
    model = PublishTab
    template_name = 'regabitur/submit/bak_ofo_up.html'

    def get_context_data(self, **kwargs):
        """Передаем записи с БАК ОФО true """
        context = super().get_context_data(**kwargs)
        all_publish = PublishTab.objects.filter(bak_ofo_up=True)
        context["list"] = all_publish
        return context


class BacZfoGp(ListView):
    """БАК ЗФО ГП"""
    model = PublishTab
    template_name = 'regabitur/submit/bak_zfo_gp.html'

    def get_context_data(self, **kwargs):
        """Передаем записи с БАК ОФО true """
        context = super().get_context_data(**kwargs)
        all_publish = PublishTab.objects.filter(bak_zfo_gp=True)
        context["list"] = all_publish
        return context


class BacZfoUp(ListView):
    """БАК ЗФО УП"""
    model = PublishTab
    template_name = 'regabitur/submit/bak_zfo_up.html'

    def get_context_data(self, **kwargs):
        """Передаем записи с БАК ОФО true """
        context = super().get_context_data(**kwargs)
        all_publish = PublishTab.objects.filter(bak_zfo_up=True)
        context["list"] = all_publish
        return context


class BacOzfoGp(ListView):
    """БАК ОЗФО ГП"""
    model = PublishTab
    template_name = 'regabitur/submit/bak_ozfo_gp.html'

    def get_context_data(self, **kwargs):
        """Передаем записи с БАК ОФО true """
        context = super().get_context_data(**kwargs)
        all_publish = PublishTab.objects.filter(bak_ozfo_gp=True)
        context["list"] = all_publish
        return context


class BacOzfoUp(ListView):
    """БАК ОЗФО УП"""
    model = PublishTab
    template_name = 'regabitur/submit/bak_ozfo_up.html'

    def get_context_data(self, **kwargs):
        """Передаем записи с БАК ОФО true """
        context = super().get_context_data(**kwargs)
        all_publish = PublishTab.objects.filter(bak_ozfo_up=True)
        context["list"] = all_publish
        return context


"""
    Специалитет
"""


class SpecOfoSd(ListView):
    """СПЕЦ ОФО СД"""
    model = PublishTab
    template_name = 'regabitur/submit/spec_ofo_sd.html'

    def get_context_data(self, **kwargs):
        """Передаем записи с БАК ОФО true """
        context = super().get_context_data(**kwargs)
        all_publish = PublishTab.objects.filter(spec_ofo_sd=True)
        context["list"] = all_publish
        return context


"""
    Магистратура
"""


class MagOfoPo(ListView):
    """Маг ОФО По"""
    model = PublishTab
    template_name = 'regabitur/submit/mag_ofo_po.html'

    def get_context_data(self, **kwargs):
        """Передаем записи с БАК ОФО true """
        context = super().get_context_data(**kwargs)
        all_publish = PublishTab.objects.filter(mag_ofo_po=True)
        context["list"] = all_publish
        return context


class MagZfoPo(ListView):
    """Маг ZФО По"""
    model = PublishTab
    template_name = 'regabitur/submit/mag_zfo_po.html'

    def get_context_data(self, **kwargs):
        """Передаем записи с БАК ОФО true """
        context = super().get_context_data(**kwargs)
        all_publish = PublishTab.objects.filter(mag_zfo_po=True)
        context["list"] = all_publish
        return context


class MagOfoTp(ListView):
    """Маг OФО TП"""
    model = PublishTab
    template_name = 'regabitur/submit/mag_ofo_tp.html'

    def get_context_data(self, **kwargs):
        """Передаем записи с БАК ОФО true """
        context = super().get_context_data(**kwargs)
        all_publish = PublishTab.objects.filter(mag_ofo_tp=True)
        context["list"] = all_publish
        return context


class MagZfoTp(ListView):
    """Маг ZФО TП"""
    model = PublishTab
    template_name = 'regabitur/submit/mag_zfo_tp.html'

    def get_context_data(self, **kwargs):
        """Передаем записи с БАК ОФО true """
        context = super().get_context_data(**kwargs)
        all_publish = PublishTab.objects.filter(mag_zfo_tp=True)
        context["list"] = all_publish
        return context


"""
    Аспирантура
"""


class AspOfoTip(ListView):
    """Асп ОФО Тип"""
    model = PublishTab
    template_name = 'regabitur/submit/asp_ofo_tip.html'

    def get_context_data(self, **kwargs):
        """Передаем записи с БАК ОФО true """
        context = super().get_context_data(**kwargs)
        all_publish = PublishTab.objects.filter(asp_ofo_tip=True)
        context["list"] = all_publish
        return context


class AspZfoTip(ListView):
    """Асп ЗФО Тип"""
    model = PublishTab
    template_name = 'regabitur/submit/asp_zfo_tip.html'

    def get_context_data(self, **kwargs):
        """Передаем записи с БАК ОФО true """
        context = super().get_context_data(**kwargs)
        all_publish = PublishTab.objects.filter(asp_zfo_tip=True)
        context["list"] = all_publish
        return context


class AspOfoUp(ListView):
    """Асп ОФО УП"""
    model = PublishTab
    template_name = 'regabitur/submit/asp_ofo_up.html'

    def get_context_data(self, **kwargs):
        """Передаем записи с БАК ОФО true """
        context = super().get_context_data(**kwargs)
        all_publish = PublishTab.objects.filter(asp_ofo_up=True)
        context["list"] = all_publish
        return context


class AspZfoUp(ListView):
    """Асп ЗФО УП"""
    model = PublishTab
    template_name = 'regabitur/submit/asp_zfo_up.html'

    def get_context_data(self, **kwargs):
        """Передаем записи с БАК ОФО true """
        context = super().get_context_data(**kwargs)
        all_publish = PublishTab.objects.filter(asp_zfo_up=True)
        context["list"] = all_publish
        return context


class AspOfoKs(ListView):
    """Асп ОФО КС"""
    model = PublishTab
    template_name = 'regabitur/submit/asp_ofo_ks.html'

    def get_context_data(self, **kwargs):
        """Передаем записи с БАК ОФО true """
        context = super().get_context_data(**kwargs)
        all_publish = PublishTab.objects.filter(asp_ofo_ks=True)
        context["list"] = all_publish
        return context


class AspZfoKs(ListView):
    """Асп ЗФО КС"""
    model = PublishTab
    template_name = 'regabitur/submit/asp_zfo_ks.html'

    def get_context_data(self, **kwargs):
        """Передаем записи с БАК ОФО true """
        context = super().get_context_data(**kwargs)
        all_publish = PublishTab.objects.filter(asp_zfo_ks=True)
        context["list"] = all_publish
        return context