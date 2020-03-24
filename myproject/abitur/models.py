from django.db import models
from django.shortcuts import reverse



class News (models.Model):
    """ модель для сущности 'новость' """
    title = models.CharField(max_length=200, db_index=True)
    body = models.TextField()
    img = models.ImageField(upload_to='pictures', max_length=255, blank=True)
    slug = models.SlugField(max_length=150, unique=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    date = models.DateField()

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