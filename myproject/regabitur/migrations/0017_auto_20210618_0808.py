# Generated by Django 3.2.3 on 2021-06-18 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regabitur', '0016_auto_20210616_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publishtab',
            name='asp_ofo',
        ),
        migrations.RemoveField(
            model_name='publishtab',
            name='asp_zfo',
        ),
        migrations.RemoveField(
            model_name='publishtab',
            name='bak_ozfo_sd',
        ),
        migrations.RemoveField(
            model_name='publishtab',
            name='mag_ofo',
        ),
        migrations.RemoveField(
            model_name='publishtab',
            name='mag_zfo',
        ),
        migrations.AddField(
            model_name='customuser',
            name='date_of_doc',
            field=models.DateField(default='1970-01-01', verbose_name='Дата выдачи документа об образовании'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='name_uz',
            field=models.CharField(blank=True, default=' ', max_length=256, verbose_name='Наименование учебного заведения, которое окончил(а)'),
        ),
        migrations.AddField(
            model_name='publishtab',
            name='asp_ofo_ks',
            field=models.BooleanField(default=False, verbose_name='Опубликовать в АСП ОФО Криминалистика'),
        ),
        migrations.AddField(
            model_name='publishtab',
            name='asp_ofo_tip',
            field=models.BooleanField(default=False, verbose_name='Опубликовать в АСП ОФО Теор. и истор.'),
        ),
        migrations.AddField(
            model_name='publishtab',
            name='asp_ofo_up',
            field=models.BooleanField(default=False, verbose_name='Опубликовать в АСП ОФО Уголовный проц.'),
        ),
        migrations.AddField(
            model_name='publishtab',
            name='asp_zfo_ks',
            field=models.BooleanField(default=False, verbose_name='Опубликовать в АСП ЗФО Криминалистика'),
        ),
        migrations.AddField(
            model_name='publishtab',
            name='asp_zfo_tip',
            field=models.BooleanField(default=False, verbose_name='Опубликовать в АСП ЗФО Теор. и истор.'),
        ),
        migrations.AddField(
            model_name='publishtab',
            name='asp_zfo_up',
            field=models.BooleanField(default=False, verbose_name='Опубликовать в АСП ЗФО Уголовный проц'),
        ),
        migrations.AddField(
            model_name='publishtab',
            name='bak_ofo_up',
            field=models.BooleanField(default=False, verbose_name='Опубликовать в БАК ОФО УП'),
        ),
        migrations.AddField(
            model_name='publishtab',
            name='bak_ozfo_gp',
            field=models.BooleanField(default=False, verbose_name='Опубликовать в БАК ОЗФО ГП'),
        ),
        migrations.AddField(
            model_name='publishtab',
            name='bak_ozfo_up',
            field=models.BooleanField(default=False, verbose_name='Опубликовать в БАК ОЗФО УП'),
        ),
        migrations.AddField(
            model_name='publishtab',
            name='bak_zfo_gp',
            field=models.BooleanField(default=False, verbose_name='Опубликовать в БАК ЗФО ГП'),
        ),
        migrations.AddField(
            model_name='publishtab',
            name='date_pub',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='publishtab',
            name='mag_ofo_po',
            field=models.BooleanField(default=False, verbose_name='Опубликовать в МАГ ОФО Прав. обеспеч.'),
        ),
        migrations.AddField(
            model_name='publishtab',
            name='mag_ofo_tp',
            field=models.BooleanField(default=False, verbose_name='Опубликовать в МАГ ОФО Теор. и практ.'),
        ),
        migrations.AddField(
            model_name='publishtab',
            name='mag_zfo_po',
            field=models.BooleanField(default=False, verbose_name='Опубликовать в МАГ ЗФО Прав. обеспеч.'),
        ),
        migrations.AddField(
            model_name='publishtab',
            name='mag_zfo_tp',
            field=models.BooleanField(default=False, verbose_name='Опубликовать в МАГ ЗФО Теор. и практ.'),
        ),
        migrations.AddField(
            model_name='publishtab',
            name='spec_ofo_sd',
            field=models.BooleanField(default=False, verbose_name='Опубликовать в СПЕЦ ОФО Судеб. деят.'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.CharField(blank=True, default=' ', max_length=400, verbose_name='Адрес регистрации (по паспорту)'),
        ),
        migrations.AlterField(
            model_name='publishtab',
            name='bak_ofo_gp',
            field=models.BooleanField(default=False, verbose_name='Опубликовать в БАК ОФО ГП'),
        ),
        migrations.AlterField(
            model_name='publishtab',
            name='bak_zfo_up',
            field=models.BooleanField(default=False, verbose_name='Опубликовать в БАК ЗФО УП'),
        ),
    ]