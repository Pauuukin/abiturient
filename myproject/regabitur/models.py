from os import urandom

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponse



def user_directory_path(instance, filename):
    """функция для записи файлов в папки с ф.и. абитуриента"""
    # file will be uploaded to MEDIA_ROOT/user_<id> + full_name
    filename = filename + str(urandom(8))
    return '{0}_{1}/{2}'.format(instance.user.pk, instance.user.get_full_name(), filename)

# Create your models here.


class CustomUser(models.Model):
    """Расширение для базового класса User"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='', verbose_name='Абитуриент', related_name='custom')
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    patronymic = models.CharField(verbose_name="Отчество (при наличии)", max_length=80, default='', blank=True)
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=15, default='')
    status_list = (
        ('error', 'Вероятно, вы указали неверные данные электронной почты или номер телефона. '
                  'Пожалуйста, свяжитесь с сотрудниками академии по телефону'),
        ('no', 'Документы не поданы'),
        ('send',
         'Документы отправлены и ждут обработки сотрудниками приемной комисси'),
        ('working', 'Документы находятся в обработке'),
        ('success', 'Документы обработаны и приняты'),
        ('back', 'Документы отозваны')
    )
    # статус заявки
    sending_status = models.CharField(max_length=256, verbose_name="Статус заявки", choices=status_list, default='no')
    # статус отправки документов
    complete_flag = models.BooleanField(default=False, verbose_name="Документы отправлены?:")
    # статус принятия соглашения о персональных данных
    agreement_flag = models.BooleanField(default=False, verbose_name="Соглашение:")
    work_flag = models.BooleanField(default=False, verbose_name="Взят в работу:")
    success_flag = models.BooleanField(default=False, verbose_name="Отработан:")

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Абитуриент'
        verbose_name_plural = 'Абитуриента'


class DocumentUser(models.Model):
    """модель БД для подачи документов"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Абитуриент", default='')
    date_pub = models.DateTimeField(auto_now=True, blank=True)

    # лист для дроп меню документов
    document_list = (
        ('Заявление', 'Заявление'),
        ('Учетная карточка', 'Учетная карточка'),
        ('Согласие на зачисление', 'Согласие на зачисление'),
        ('Обработка персональных данных', 'Обработка персональных данных'),
        ('Фото (3х4)', 'Фото (3х4)'),
        ('Документ, удостоверяющий личность', 'Документ, удостоверяющий личность'),
        ('Временная регистрация', 'Временная регистрация(при наличии в СПб)'),
        ('Документ об образовании', 'Документ об образовании'),
        ('мед.справка', 'Медицинская справка по форме 086-У'),
        ('Прививочный сертификат', 'Прививочный сертификат'),
        ('Военный билет или приписное', 'Военный билет или приписное удостоверение'),
        ('Снилс', 'Снилс'),
        ('Индивидуальные достижения', 'Индивидуальные достижения'),
    )

    name_doc = models.CharField(max_length=256, verbose_name="Название документа", choices=document_list)
    doc = models.FileField(upload_to=user_directory_path, verbose_name="Загрузить документ")

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Документы абитуриентов'
        verbose_name_plural = 'Документы абитуриентов'

    def delete(self, *args, **kwargs):
        """Функция удаления файла с сервера при удалении записи файла из БД"""
        # До удаления записи получаем необходимую информацию
        storage, path = self.doc.storage, self.doc.path
        # Удаляем сначала модель ( объект )
        super(DocumentUser, self).delete(*args, **kwargs)
        # Потом удаляем сам файл
        storage.delete(path)

