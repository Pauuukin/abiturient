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


class NewsFile(models.Model):
    """ модель для сущности 'файлы для новости' """
    name_file = models.CharField(max_length=100, default="Открыть")
    file = models.FileField(upload_to='files')
    news = models.ForeignKey('News', on_delete=models.CASCADE, related_name='linked_file')

    def __str__(self):
        """переопределяем метод String"""
        return self.name_file



class EducationalForm(models.Model):
    """модель для сущности 'Форма обучения' """
    name_educational_form = models.CharField(max_length=64)

    def __str__(self):
        """переопределяем метод String"""
        return self.name_educational_form



class Orders(models.Model):
    """ модель для сущности 'Приказы' """
    name_order = models.CharField(max_length=256)
    number_order = models.CharField(max_length=64)
    educational_form = models.ForeignKey('EducationalForm', on_delete=models.PROTECT, related_name='linked_orders')
    date_pub = models.DateTimeField(auto_now_add=True)
    date_order = models.DateField()
    file = models.FileField(upload_to='files')

    def __str__(self):
        """переопределяем метод String"""
        return self.name_order
