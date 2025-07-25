# Generated by Django 5.1.6 on 2025-03-19 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tkd_online_forum', '0003_tag_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Активно'),
        ),
        migrations.AddField(
            model_name='news',
            name='cost',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='news',
            name='date_begin',
            field=models.DateField(blank=True, null=True, verbose_name='Дата начала'),
        ),
        migrations.AddField(
            model_name='news',
            name='date_end',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания'),
        ),
        migrations.AddField(
            model_name='news',
            name='time_begin',
            field=models.TimeField(blank=True, null=True, verbose_name='Время начала'),
        ),
        migrations.AddField(
            model_name='news',
            name='time_end',
            field=models.TimeField(blank=True, null=True, verbose_name='Время начала'),
        ),
    ]
