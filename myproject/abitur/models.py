from django.db import models

# Create your models here.


class News (models.Model):
    title = models.CharField(max_length=200, db_index=True)
    body = models.TextField()
    img = models.ImageField(upload_to='pictures/%Y/%m/', max_length=255)
    date_pub = models.DateTimeField(auto_now_add=True)
    date = models.DateField()

    def __str__(self):
        return '{}'.format(self.title)

