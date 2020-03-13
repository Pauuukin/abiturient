from django.db import models
from django.shortcuts import reverse

# Create your models here.


class News (models.Model):
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
        return '{}'.format(self.title)


class NewsFile(models.Model):
    file = models.FileField(upload_to='files')
    news = models.ForeignKey('News', on_delete=models.CASCADE)

