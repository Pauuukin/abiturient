# Generated by Django 3.0.5 on 2020-04-29 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abitur', '0002_auto_20200429_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultMag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_result', models.CharField(max_length=256)),
                ('number_result', models.CharField(max_length=64)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('date_result', models.DateField()),
                ('file', models.FileField(upload_to='files')),
                ('educational_form', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='linked_results', to='abitur.EducationalFormMag')),
            ],
            options={
                'verbose_name': 'Результаты вступительных испытаний (Магистратура)',
                'verbose_name_plural': 'Результаты вступительных испытаний - МАГИСТРАТУРА',
            },
        ),
        migrations.CreateModel(
            name='ResultAsp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_result', models.CharField(max_length=256)),
                ('number_result', models.CharField(max_length=64)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('date_result', models.DateField()),
                ('file', models.FileField(upload_to='files')),
                ('educational_form', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='linked_results', to='abitur.EducationalFormAsp')),
            ],
            options={
                'verbose_name': 'Результаты вступительных испытаний (Аспирантура)',
                'verbose_name_plural': 'Результаты вступительных испытаний - АСПИРАНТУРА',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_result', models.CharField(max_length=256)),
                ('number_result', models.CharField(max_length=64)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('date_result', models.DateField()),
                ('file', models.FileField(upload_to='files')),
                ('educational_form', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='linked_results', to='abitur.EducationalForm')),
            ],
            options={
                'verbose_name': 'Результаты вступительных испытаний (бакалавриат)',
                'verbose_name_plural': 'Результаты вступительных испытаний - БАКАЛАВРИАТ',
            },
        ),
    ]
