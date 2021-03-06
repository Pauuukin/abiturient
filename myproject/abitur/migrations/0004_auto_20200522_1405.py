# Generated by Django 3.0.5 on 2020-05-22 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abitur', '0003_result_resultasp_resultmag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body',
            field=models.TextField(verbose_name='Основной текст'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date_pub',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='news',
            name='img',
            field=models.ImageField(blank=True, default='static/image/logo.png', max_length=255, upload_to='pictures', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='newsfile',
            name='file',
            field=models.FileField(upload_to='files', verbose_name='Прикрепить файл'),
        ),
        migrations.AlterField(
            model_name='newsfile',
            name='name_file',
            field=models.CharField(default='Открыть', max_length=100, verbose_name='Имя файла (по умолчанию="Открыть"'),
        ),
        migrations.AlterField(
            model_name='newsfile',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linked_file', to='abitur.News', verbose_name='Выберите новость, для которой прикрепляется файл'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date_order',
            field=models.DateField(verbose_name='Дата создания приказа'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='educational_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='linked_orders', to='abitur.EducationalForm', verbose_name='Форма обучения'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='file',
            field=models.FileField(upload_to='files', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='name_order',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='number_order',
            field=models.CharField(max_length=64, verbose_name='Номер документа'),
        ),
        migrations.AlterField(
            model_name='ordersasp',
            name='date_order',
            field=models.DateField(verbose_name='Дата создания приказа'),
        ),
        migrations.AlterField(
            model_name='ordersasp',
            name='educational_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='linked_orders', to='abitur.EducationalFormAsp', verbose_name='Форма обучения'),
        ),
        migrations.AlterField(
            model_name='ordersasp',
            name='file',
            field=models.FileField(upload_to='files', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='ordersasp',
            name='name_order',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='ordersasp',
            name='number_order',
            field=models.CharField(max_length=64, verbose_name='Номер документа'),
        ),
        migrations.AlterField(
            model_name='ordersmag',
            name='date_order',
            field=models.DateField(verbose_name='Дата создания приказа'),
        ),
        migrations.AlterField(
            model_name='ordersmag',
            name='educational_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='linked_orders', to='abitur.EducationalFormMag', verbose_name='Форма обучения'),
        ),
        migrations.AlterField(
            model_name='ordersmag',
            name='file',
            field=models.FileField(upload_to='files', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='ordersmag',
            name='name_order',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='ordersmag',
            name='number_order',
            field=models.CharField(max_length=64, verbose_name='Номер документа'),
        ),
        migrations.AlterField(
            model_name='recommendedlist',
            name='date_order',
            field=models.DateField(verbose_name='Дата создания приказа'),
        ),
        migrations.AlterField(
            model_name='recommendedlist',
            name='educational_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='linked_rec_list', to='abitur.EducationalForm', verbose_name='Форма обучения'),
        ),
        migrations.AlterField(
            model_name='recommendedlist',
            name='file',
            field=models.FileField(upload_to='files', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='recommendedlist',
            name='name_rec_list',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='recommendedlistasp',
            name='date_order',
            field=models.DateField(verbose_name='Дата создания приказа'),
        ),
        migrations.AlterField(
            model_name='recommendedlistasp',
            name='educational_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='linked_rec_list', to='abitur.EducationalFormAsp', verbose_name='Форма обучения'),
        ),
        migrations.AlterField(
            model_name='recommendedlistasp',
            name='file',
            field=models.FileField(upload_to='files', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='recommendedlistasp',
            name='name_rec_list',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='recommendedlistmag',
            name='date_order',
            field=models.DateField(verbose_name='Дата создания приказа'),
        ),
        migrations.AlterField(
            model_name='recommendedlistmag',
            name='educational_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='linked_rec_list', to='abitur.EducationalFormMag', verbose_name='Форма обучения'),
        ),
        migrations.AlterField(
            model_name='recommendedlistmag',
            name='file',
            field=models.FileField(upload_to='files', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='recommendedlistmag',
            name='name_rec_list',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='result',
            name='date_result',
            field=models.DateField(verbose_name='Дата создания приказа'),
        ),
        migrations.AlterField(
            model_name='result',
            name='educational_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='linked_results', to='abitur.EducationalForm', verbose_name='Форма обучения'),
        ),
        migrations.AlterField(
            model_name='result',
            name='file',
            field=models.FileField(upload_to='files', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='result',
            name='name_result',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='result',
            name='number_result',
            field=models.CharField(max_length=64, verbose_name='Номер документа'),
        ),
        migrations.AlterField(
            model_name='resultasp',
            name='date_result',
            field=models.DateField(verbose_name='Дата создания приказа'),
        ),
        migrations.AlterField(
            model_name='resultasp',
            name='educational_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='linked_results', to='abitur.EducationalFormAsp', verbose_name='Форма обучения'),
        ),
        migrations.AlterField(
            model_name='resultasp',
            name='file',
            field=models.FileField(upload_to='files', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='resultasp',
            name='name_result',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='resultasp',
            name='number_result',
            field=models.CharField(max_length=64, verbose_name='Номер документа'),
        ),
        migrations.AlterField(
            model_name='resultmag',
            name='date_result',
            field=models.DateField(verbose_name='Дата создания приказа'),
        ),
        migrations.AlterField(
            model_name='resultmag',
            name='educational_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='linked_results', to='abitur.EducationalFormMag', verbose_name='Форма обучения'),
        ),
        migrations.AlterField(
            model_name='resultmag',
            name='file',
            field=models.FileField(upload_to='files', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='resultmag',
            name='name_result',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='resultmag',
            name='number_result',
            field=models.CharField(max_length=64, verbose_name='Номер документа'),
        ),
        migrations.AlterField(
            model_name='submitdoc',
            name='date_order',
            field=models.DateField(verbose_name='Дата создания приказа'),
        ),
        migrations.AlterField(
            model_name='submitdoc',
            name='educational_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='linked_submit_doc', to='abitur.EducationalForm', verbose_name='Форма обучения'),
        ),
        migrations.AlterField(
            model_name='submitdoc',
            name='file',
            field=models.FileField(upload_to='files', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='submitdoc',
            name='name_submit_doc',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='submitdocasp',
            name='date_order',
            field=models.DateField(verbose_name='Дата создания приказа'),
        ),
        migrations.AlterField(
            model_name='submitdocasp',
            name='educational_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='linked_submit_doc', to='abitur.EducationalFormAsp', verbose_name='Форма обучения'),
        ),
        migrations.AlterField(
            model_name='submitdocasp',
            name='file',
            field=models.FileField(upload_to='files', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='submitdocasp',
            name='name_submit_doc',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='submitdocmag',
            name='date_order',
            field=models.DateField(verbose_name='Дата создания приказа'),
        ),
        migrations.AlterField(
            model_name='submitdocmag',
            name='educational_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='linked_submit_doc', to='abitur.EducationalFormMag', verbose_name='Форма обучения'),
        ),
        migrations.AlterField(
            model_name='submitdocmag',
            name='file',
            field=models.FileField(upload_to='files', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='submitdocmag',
            name='name_submit_doc',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
    ]
