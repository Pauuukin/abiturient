from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    """функция для записи файлов в папки с ф.и. абитуриента"""
    # file will be uploaded to MEDIA_ROOT/user_<id> + full_name
    filename = '{0}: {1}'.format(instance.name_doc, filename)
    return '{0}_{1}/{2}'.format(instance.user.pk, instance.user.get_full_name(), filename)


class CustomUser(models.Model):
    """Расширение для базового класса User"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='',
                                verbose_name='Абитуриент', related_name='custom')
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    patronymic = models.CharField(verbose_name="Отчество (при наличии)", max_length=80,
                                  default='', blank=True)
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
    sending_status = models.CharField(max_length=256, verbose_name="Статус заявки",
                                      choices=status_list, default='no')
    # статус отправки документов
    complete_flag = models.BooleanField(default=False, verbose_name="Документы отправлены?:")
    # статус принятия соглашения о персональных данных
    agreement_flag = models.BooleanField(default=False, verbose_name="Соглашение:")
    work_flag = models.BooleanField(default=False, verbose_name="Взят в работу:")
    success_flag = models.BooleanField(default=False, verbose_name="Отработан:")
    comment_admin = models.TextField(verbose_name="Комментарий для внутренней работы", blank=True)

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Абитуриент'
        verbose_name_plural = 'Абитуриента'

    def __str__(self):
        """Переопределяем метод String"""
        name_field = ("id = " + str(self.user.id) + " / " + self.user.get_full_name())
        return name_field


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

    name_doc = models.CharField(max_length=256, verbose_name="Название документа",
                                choices=document_list)
    doc = models.FileField(upload_to=user_directory_path, verbose_name="Загрузить документ")
    address = models.CharField(max_length=400, verbose_name="Адрес прописки", blank=True, default=' ')
    passport = models.CharField(max_length=20, verbose_name="Паспортные данные(серия-номер)", blank=True, default=' ')
    snils = models.CharField(max_length=32, verbose_name="Номер снился", blank=True, default=' ')

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


class ChoicesProfile(models.Model):
    """Выбор профиля обучения"""
    description = models.CharField(max_length=256)

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Профиль обучения'
        verbose_name_plural = 'Профили обучения'

    def __str__(self):
        return self.description


class AdditionalInfo(models.Model):
    """Класс с дополнительной информацией о пользователе (прием 21/22)"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь", default='', related_name='addition')
    education_profile = models.ManyToManyField(ChoicesProfile, verbose_name="Форма обучения")


    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Выбранные профили обучения'
        verbose_name_plural = 'Выбранные профили обучения'


class PublishTab(models.Model):
    """Публикация пользователей в списках подавших документы"""

    choice_field = (
        ('ЕГЭ', 'ЕГЭ'),
        ('Вступительные испытания', 'Вступительные испытания'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь", default='')
    individual_str = models.CharField(max_length=32, blank=True)
    test_type = models.CharField(max_length=256, verbose_name="Вступительные испытания",
                                 choices=choice_field)
    bak_ofo_gp = models.BooleanField(default=False, verbose_name="Опубликовать в БАК ОФО")
    bak_zfo_up = models.BooleanField(default=False, verbose_name="Опубликовать в БАК ЗФО")
    bak_ozfo_sd = models.BooleanField(default=False, verbose_name="Опубликовать в БАК ОЗФО")
    mag_ofo = models.BooleanField(default=False, verbose_name="Опубликовать в МАГ ОФО")
    mag_zfo = models.BooleanField(default=False, verbose_name="Опубликовать в МАГ ЗФО")
    asp_ofo = models.BooleanField(default=False, verbose_name="Опубликовать в АСП ОФО")
    asp_zfo = models.BooleanField(default=False, verbose_name="Опубликовать в АСП ЗФО")

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Опубликовать в списки подавших'
        verbose_name_plural = 'Опубликовать в списки подавших'

    def __str__(self):
        return self.user.get_full_name()
