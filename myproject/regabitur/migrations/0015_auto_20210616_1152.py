# Generated by Django 3.2.3 on 2021-06-16 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regabitur', '0014_auto_20210616_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentuser',
            name='address',
        ),
        migrations.RemoveField(
            model_name='documentuser',
            name='passport',
        ),
        migrations.RemoveField(
            model_name='documentuser',
            name='snils',
        ),
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(blank=True, default=' ', max_length=400, verbose_name='Адрес прописки'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='passport',
            field=models.CharField(blank=True, default=' ', max_length=20, verbose_name='Паспортные данные(серия-номер)'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='snils',
            field=models.CharField(blank=True, default=' ', max_length=32, verbose_name='Номер снился'),
        ),
    ]