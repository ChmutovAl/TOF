from tabnanny import verbose

from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    gen = (('Мужской', 'Мужской'),
           ('Женский', 'Женский'))
    mid_name = models.CharField(max_length=120, null=True, blank=True, verbose_name='Отчество')
    sex = models.CharField(max_length=7, choices=gen, default=gen[0][0], verbose_name='Пол')
    email = models.EmailField(unique=True, null=True, blank=False, verbose_name='Email')
    region = models.CharField(max_length=100, null=True, blank=False, verbose_name='Регион')
    federation = models.ForeignKey('Federation', on_delete=models.SET_NULL, null=True, verbose_name='Федерация')
    club = models.CharField(max_length=30, null=True, blank=False, verbose_name='Клуб')
    bd = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=False, verbose_name='Дата рождения')
    belt = models.ForeignKey('Belt', on_delete=models.SET_NULL, null=True, blank=False, verbose_name='Пояс')
    qual = models.ForeignKey('Qualification', on_delete=models.SET_NULL, null=True, blank=False,
                             verbose_name='Квалификация')
    org = models.BooleanField(default=False, verbose_name='Организация')
    admin = models.BooleanField(default=False, verbose_name='Админ')

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.mid_name


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Event(models.Model):
    event_type = (('Соревнование', 'Соревнование'),
                 ('Семинар', 'Семинар'))
    name = models.CharField(max_length=20, verbose_name='Название')
    date_begin = models.DateField(auto_now=False, auto_now_add=False, null=False, blank=False, verbose_name='Дата начала')
    date_end = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name='Дата окончания')
    file = models.FileField(upload_to='competitions/', null=True, blank=True, verbose_name='Протокол')
    time_begin = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name='Время начала')
    time_end = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name='Время начала')
    comment = models.CharField(max_length=250, verbose_name='Описание')
    active = models.BooleanField(default=False, verbose_name='Активно')
    cost = models.IntegerField(verbose_name='Цена')
    type = models.CharField(max_length=30, choices=event_type, default=event_type[0][0], verbose_name='Тип мероприятия')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class AppCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    fio = models.CharField(max_length=100, null=False, blank=False, verbose_name='ФИО')
    file = models.FileField(upload_to='cards/', null=True, blank=True, verbose_name='Видео')
    comment = models.CharField(max_length=100, null=True, blank=True,verbose_name='Комментарий')
    event = models.ForeignKey(Event, on_delete=models.PROTECT, null=False, blank=False,
                                    verbose_name='Мероприятие')
    score = models.IntegerField(null=True, blank=True, verbose_name='Баллы')
    anon = models.BooleanField(default=False, verbose_name='Анон')
    status = models.BooleanField(default=False, verbose_name='Статус оплаты')
    admin_comment = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий админа')

    def __str__(self):
        return self.fio + ' ' + self.event.name


    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Federation(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, verbose_name='Название')

    class Meta:
        verbose_name = 'Федерация'
        verbose_name_plural = 'Федерации'


class Belt(models.Model):
    name = models.CharField(max_length=8, null=False, blank=False, verbose_name='Название')

    class Meta:
        verbose_name = 'Пояс'
        verbose_name_plural = 'Пояса'


class Qualification(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, verbose_name='Название')

    class Meta:
        verbose_name = 'Разряд'
        verbose_name_plural = 'Разряды'