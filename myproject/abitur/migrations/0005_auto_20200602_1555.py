# Generated by Django 3.0.5 on 2020-06-02 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abitur', '0004_auto_20200522_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='img',
            field=models.ImageField(blank=True, default='pictures/base.jpg', max_length=255, upload_to='pictures', verbose_name='Изображение'),
        ),
    ]
