# Generated by Django 3.0.5 on 2020-04-29 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abitur', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_educational_form', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='EducationalFormAsp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_educational_form', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='EducationalFormMag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_educational_form', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Добавить новости'},
        ),
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='img',
            field=models.ImageField(blank=True, max_length=255, upload_to='pictures'),
        ),
        migrations.CreateModel(
            name='SubmitDocMag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_submit_doc', models.CharField(max_length=256)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('date_order', models.DateField()),
                ('file', models.FileField(upload_to='files')),
                ('educational_form', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='linked_submit_doc', to='abitur.EducationalFormMag')),
            ],
            options={
                'verbose_name': 'Списки подавших документы(магистратура)',
                'verbose_name_plural': 'Списки подавших документы - МАГИСТРАТУРА',
            },
        ),
        migrations.CreateModel(
            name='SubmitDocAsp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_submit_doc', models.CharField(max_length=256)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('date_order', models.DateField()),
                ('file', models.FileField(upload_to='files')),
                ('educational_form', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='linked_submit_doc', to='abitur.EducationalFormAsp')),
            ],
            options={
                'verbose_name': 'Списки подавших документы(аспирантура)',
                'verbose_name_plural': 'Списки подавших документы - АСПИРАНТУРА',
            },
        ),
        migrations.CreateModel(
            name='SubmitDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_submit_doc', models.CharField(max_length=256)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('date_order', models.DateField()),
                ('file', models.FileField(upload_to='files')),
                ('educational_form', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='linked_submit_doc', to='abitur.EducationalForm')),
            ],
            options={
                'verbose_name': 'Списки подавших документы(бакалавриат)',
                'verbose_name_plural': 'Списки подавших документы - БАКАЛАВРИАТ',
            },
        ),
        migrations.CreateModel(
            name='RecommendedListMag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_rec_list', models.CharField(max_length=256)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('date_order', models.DateField()),
                ('file', models.FileField(upload_to='files')),
                ('educational_form', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='linked_rec_list', to='abitur.EducationalFormMag')),
            ],
            options={
                'verbose_name': 'Списки рекомендованных к зачислению(магистратура)',
                'verbose_name_plural': 'Списки рекомендованных к зачислению - МАГИСТРАТУРА',
            },
        ),
        migrations.CreateModel(
            name='RecommendedListAsp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_rec_list', models.CharField(max_length=256)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('date_order', models.DateField()),
                ('file', models.FileField(upload_to='files')),
                ('educational_form', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='linked_rec_list', to='abitur.EducationalFormAsp')),
            ],
            options={
                'verbose_name': 'Списки рекомендованных к зачислению(аспирантура)',
                'verbose_name_plural': 'Списки рекомендованных к зачислению - АСПИРАНТУРА',
            },
        ),
        migrations.CreateModel(
            name='RecommendedList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_rec_list', models.CharField(max_length=256)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('date_order', models.DateField()),
                ('file', models.FileField(upload_to='files')),
                ('educational_form', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='linked_rec_list', to='abitur.EducationalForm')),
            ],
            options={
                'verbose_name': 'Списки рекомендованных к зачислению(бакалавриат)',
                'verbose_name_plural': 'Списки рекомендованных к зачислению - БАКАЛАВРИАТ',
            },
        ),
        migrations.CreateModel(
            name='OrdersMag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_order', models.CharField(max_length=256)),
                ('number_order', models.CharField(max_length=64)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('date_order', models.DateField()),
                ('file', models.FileField(upload_to='files')),
                ('educational_form', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='linked_orders', to='abitur.EducationalFormMag')),
            ],
            options={
                'verbose_name': 'Приказ о зачислении(магистратура)',
                'verbose_name_plural': 'Приказы о зачислении - МАГИСТРАТУРА',
            },
        ),
        migrations.CreateModel(
            name='OrdersAsp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_order', models.CharField(max_length=256)),
                ('number_order', models.CharField(max_length=64)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('date_order', models.DateField()),
                ('file', models.FileField(upload_to='files')),
                ('educational_form', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='linked_orders', to='abitur.EducationalFormAsp')),
            ],
            options={
                'verbose_name': 'Приказ о зачислении(аспирантура)',
                'verbose_name_plural': 'Приказы о зачислении - АСПИРАНТУРА',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_order', models.CharField(max_length=256)),
                ('number_order', models.CharField(max_length=64)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('date_order', models.DateField()),
                ('file', models.FileField(upload_to='files')),
                ('educational_form', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='linked_orders', to='abitur.EducationalForm')),
            ],
            options={
                'verbose_name': 'Приказ о зачислении(бакалавриат)',
                'verbose_name_plural': 'Приказы о зачислении - БАКАЛАВРИАТ',
            },
        ),
        migrations.CreateModel(
            name='NewsFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_file', models.CharField(default='Открыть', max_length=100)),
                ('file', models.FileField(upload_to='files')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linked_file', to='abitur.News')),
            ],
            options={
                'verbose_name': 'Файл для новости',
                'verbose_name_plural': 'Добавить файлы для новости',
            },
        ),
    ]
