# Generated by Django 3.0.3 on 2020-06-20 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regabitur', '0004_auto_20200620_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='success_flag',
            field=models.BooleanField(default=False, verbose_name='Отработан:'),
        ),
    ]
