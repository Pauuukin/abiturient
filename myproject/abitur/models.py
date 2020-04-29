from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from transliterate import translit
from time import time




class News (models.Model):
    """ модель для сущности 'новость' """
    title = models.CharField(max_length=200, db_index=True)
    body = models.TextField()
    img = models.ImageField(upload_to='pictures', max_length=255, blank=True)
    slug = models.SlugField(max_length=150, default="", unique=True, blank=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    date = models.DateField()

    def save(self, *args, **kwargs):
        """переопределяем метод save"""
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """возвращает ссылку на конкретный экземпляр класса"""
        return reverse('news_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        """Переопределяем метод String"""
        return self.title

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Новость'
        verbose_name_plural = 'Добавить новости'


def gen_slug(s):
    """автогенерация слагов"""
    str1 = translit(s, "ru", reversed=True)
    new_slug = slugify(str1, allow_unicode=True)
    return new_slug + '-' + str(int(time()))



class NewsFile(models.Model):
    """ модель для сущности 'файлы для новости' """
    name_file = models.CharField(max_length=100, default="Открыть")
    file = models.FileField(upload_to='files')
    news = models.ForeignKey('News', on_delete=models.CASCADE, related_name='linked_file')

    def __str__(self):
        """переопределяем метод String"""
        return self.name_file

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Файл для новости'
        verbose_name_plural = 'Добавить файлы для новости'

# Для бакалавриата -->


class EducationalForm(models.Model):
    """модель для сущности 'Форма обучения' """
    name_educational_form = models.CharField(max_length=64)

    def __str__(self):
        """переопределяем метод String"""
        return self.name_educational_form


class Orders(models.Model):
    """ модель для сущности 'Приказы БАКАЛАВРИАТ' """
    name_order = models.CharField(max_length=256)
    number_order = models.CharField(max_length=64)
    educational_form = models.ForeignKey('EducationalForm', on_delete=models.PROTECT, related_name='linked_orders')
    date_pub = models.DateTimeField(auto_now_add=True)
    date_order = models.DateField()
    file = models.FileField(upload_to='files')

    def __str__(self):
        """переопределяем метод String"""
        return self.name_order

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Приказ о зачислении(бакалавриат)'
        verbose_name_plural = 'Приказы о зачислении - БАКАЛАВРИАТ'


class Result(models.Model):
    """ модель для сущности 'Результаты вступительных БАКАЛАВРИАТ' """
    name_result = models.CharField(max_length=256)
    number_result = models.CharField(max_length=64)
    educational_form = models.ForeignKey('EducationalForm', on_delete=models.PROTECT, related_name='linked_results')
    date_pub = models.DateTimeField(auto_now_add=True)
    date_result = models.DateField()
    file = models.FileField(upload_to='files')

    def __str__(self):
        """переопределяем метод String"""
        return self.name_result

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Результаты вступительных испытаний (бакалавриат)'
        verbose_name_plural = 'Результаты вступительных испытаний - БАКАЛАВРИАТ'


class RecommendedList(models.Model):
    """ модель для сущности 'Рекомендованные к зачислению БАКАЛАВРИАТ' """
    name_rec_list = models.CharField(max_length=256)
    educational_form = models.ForeignKey('EducationalForm', on_delete=models.PROTECT, related_name='linked_rec_list')
    date_pub = models.DateTimeField(auto_now_add=True)
    date_order = models.DateField()
    file = models.FileField(upload_to='files')

    def __str__(self):
        """переопределяем метод String"""
        return self.name_rec_list

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Списки рекомендованных к зачислению(бакалавриат)'
        verbose_name_plural = 'Списки рекомендованных к зачислению - БАКАЛАВРИАТ'


class SubmitDoc(models.Model):
    """ модель для сущности 'Подавшие документы БАКАЛАВРИАТ' """
    name_submit_doc = models.CharField(max_length=256)
    educational_form = models.ForeignKey('EducationalForm', on_delete=models.PROTECT, related_name='linked_submit_doc')
    date_pub = models.DateTimeField(auto_now_add=True)
    date_order = models.DateField()
    file = models.FileField(upload_to='files')

    def __str__(self):
        """переопределяем метод String"""
        return self.name_submit_doc

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Списки подавших документы(бакалавриат)'
        verbose_name_plural = 'Списки подавших документы - БАКАЛАВРИАТ'

#<--

#Для Магистратуры -->


class EducationalFormMag(models.Model):
    """модель для сущности 'Форма обучения ' """
    name_educational_form = models.CharField(max_length=64)

    def __str__(self):
        """переопределяем метод String"""
        return self.name_educational_form


class OrdersMag(models.Model):
    """ модель для сущности 'Приказы Магистратура' """
    name_order = models.CharField(max_length=256)
    number_order = models.CharField(max_length=64)
    educational_form = models.ForeignKey('EducationalFormMag', on_delete=models.PROTECT, related_name='linked_orders')
    date_pub = models.DateTimeField(auto_now_add=True)
    date_order = models.DateField()
    file = models.FileField(upload_to='files')

    def __str__(self):
        """переопределяем метод String"""
        return self.name_order

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Приказ о зачислении(магистратура)'
        verbose_name_plural = 'Приказы о зачислении - МАГИСТРАТУРА'


class ResultMag(models.Model):
    """ модель для сущности 'Результаты вступительных МАГИСТРАТУРА' """
    name_result = models.CharField(max_length=256)
    number_result = models.CharField(max_length=64)
    educational_form = models.ForeignKey('EducationalFormMag', on_delete=models.PROTECT, related_name='linked_results')
    date_pub = models.DateTimeField(auto_now_add=True)
    date_result = models.DateField()
    file = models.FileField(upload_to='files')

    def __str__(self):
        """переопределяем метод String"""
        return self.name_result

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Результаты вступительных испытаний (Магистратура)'
        verbose_name_plural = 'Результаты вступительных испытаний - МАГИСТРАТУРА'



class RecommendedListMag(models.Model):
    """ модель для сущности 'Рекомендованные к зачислению Магистратура' """
    name_rec_list = models.CharField(max_length=256)
    educational_form = models.ForeignKey('EducationalFormMag', on_delete=models.PROTECT, related_name='linked_rec_list')
    date_pub = models.DateTimeField(auto_now_add=True)
    date_order = models.DateField()
    file = models.FileField(upload_to='files')

    def __str__(self):
        """переопределяем метод String"""
        return self.name_rec_list

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Списки рекомендованных к зачислению(магистратура)'
        verbose_name_plural = 'Списки рекомендованных к зачислению - МАГИСТРАТУРА'


class SubmitDocMag(models.Model):
    """ модель для сущности 'Подавшие документы Магистратура' """
    name_submit_doc = models.CharField(max_length=256)
    educational_form = models.ForeignKey('EducationalFormMag', on_delete=models.PROTECT,
                                         related_name='linked_submit_doc')
    date_pub = models.DateTimeField(auto_now_add=True)
    date_order = models.DateField()
    file = models.FileField(upload_to='files')

    def __str__(self):
        """переопределяем метод String"""
        return self.name_submit_doc

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Списки подавших документы(магистратура)'
        verbose_name_plural = 'Списки подавших документы - МАГИСТРАТУРА'

#<--
#Для Аспирантуры -->


class EducationalFormAsp(models.Model):
    """модель для сущности 'Форма обучения ' """
    name_educational_form = models.CharField(max_length=64)

    def __str__(self):
        """переопределяем метод String"""
        return self.name_educational_form


class OrdersAsp(models.Model):
    """ модель для сущности 'Приказы Магистратура' """
    name_order = models.CharField(max_length=256)
    number_order = models.CharField(max_length=64)
    educational_form = models.ForeignKey('EducationalFormAsp', on_delete=models.PROTECT, related_name='linked_orders')
    date_pub = models.DateTimeField(auto_now_add=True)
    date_order = models.DateField()
    file = models.FileField(upload_to='files')

    def __str__(self):
        """переопределяем метод String"""
        return self.name_order

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Приказ о зачислении(аспирантура)'
        verbose_name_plural = 'Приказы о зачислении - АСПИРАНТУРА'


class ResultAsp(models.Model):
    """ модель для сущности 'Результаты вступительных АСПИРАНТУРА' """
    name_result = models.CharField(max_length=256)
    number_result = models.CharField(max_length=64)
    educational_form = models.ForeignKey('EducationalFormAsp', on_delete=models.PROTECT, related_name='linked_results')
    date_pub = models.DateTimeField(auto_now_add=True)
    date_result = models.DateField()
    file = models.FileField(upload_to='files')

    def __str__(self):
        """переопределяем метод String"""
        return self.name_result

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Результаты вступительных испытаний (Аспирантура)'
        verbose_name_plural = 'Результаты вступительных испытаний - АСПИРАНТУРА'


class RecommendedListAsp(models.Model):
    """ модель для сущности 'Рекомендованные к зачислению Магистратура' """
    name_rec_list = models.CharField(max_length=256)
    educational_form = models.ForeignKey('EducationalFormAsp', on_delete=models.PROTECT, related_name='linked_rec_list')
    date_pub = models.DateTimeField(auto_now_add=True)
    date_order = models.DateField()
    file = models.FileField(upload_to='files')

    def __str__(self):
        """переопределяем метод String"""
        return self.name_rec_list

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Списки рекомендованных к зачислению(аспирантура)'
        verbose_name_plural = 'Списки рекомендованных к зачислению - АСПИРАНТУРА'


class SubmitDocAsp(models.Model):
    """ модель для сущности 'Подавшие документы Магистратура' """
    name_submit_doc = models.CharField(max_length=256)
    educational_form = models.ForeignKey('EducationalFormAsp', on_delete=models.PROTECT,
                                         related_name='linked_submit_doc')
    date_pub = models.DateTimeField(auto_now_add=True)
    date_order = models.DateField()
    file = models.FileField(upload_to='files')

    def __str__(self):
        """переопределяем метод String"""
        return self.name_submit_doc

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Списки подавших документы(аспирантура)'
        verbose_name_plural = 'Списки подавших документы - АСПИРАНТУРА'
#<--