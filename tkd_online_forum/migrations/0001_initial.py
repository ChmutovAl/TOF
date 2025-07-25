# Generated by Django 5.1.6 on 2025-03-03 19:17

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Belt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Пояс',
                'verbose_name_plural': 'Пояса',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('date_begin', models.DateField(verbose_name='Дата начала')),
                ('date_end', models.DateField(blank=True, null=True, verbose_name='Дата окончания')),
                ('file', models.FileField(blank=True, null=True, upload_to='competitions/', verbose_name='Протокол')),
                ('time_begin', models.TimeField(blank=True, null=True, verbose_name='Время начала')),
                ('time_end', models.TimeField(blank=True, null=True, verbose_name='Время начала')),
                ('comment', models.CharField(max_length=250, verbose_name='Описание')),
                ('active', models.BooleanField(default=False, verbose_name='Активно')),
                ('cost', models.IntegerField(verbose_name='Цена')),
                ('type', models.CharField(choices=[('Соревнование', 'Соревнование'), ('Семинар', 'Семинар')], default='Соревнование', max_length=30, verbose_name='Тип мероприятия')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
        migrations.CreateModel(
            name='Federation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Федерация',
                'verbose_name_plural': 'Федерации',
            },
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Разряд',
                'verbose_name_plural': 'Разряды',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('mid_name', models.CharField(blank=True, max_length=120, null=True, verbose_name='Отчество')),
                ('sex', models.CharField(choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], default='Мужской', max_length=7, verbose_name='Пол')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('region', models.CharField(max_length=100, verbose_name='Регион')),
                ('club', models.CharField(max_length=30, verbose_name='Клуб')),
                ('bd', models.DateField(verbose_name='Дата рождения')),
                ('org', models.BooleanField(default=False, verbose_name='Организация')),
                ('admin', models.BooleanField(default=False, verbose_name='Админ')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('belt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tkd_online_forum.belt', verbose_name='Пояс')),
                ('federation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tkd_online_forum.federation', verbose_name='Федерация')),
                ('qual', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tkd_online_forum.qualification', verbose_name='Квалификация')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AppCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100, verbose_name='ФИО')),
                ('file', models.FileField(blank=True, null=True, upload_to='cards/', verbose_name='Видео')),
                ('comment', models.CharField(blank=True, max_length=100, null=True, verbose_name='Комментарий')),
                ('score', models.IntegerField(blank=True, null=True, verbose_name='Баллы')),
                ('anon', models.BooleanField(default=False, verbose_name='Анон')),
                ('status', models.BooleanField(default=False, verbose_name='Статус оплаты')),
                ('admin_comment', models.CharField(blank=True, max_length=100, null=True, verbose_name='Комментарий админа')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tkd_online_forum.event', verbose_name='Мероприятие')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
