from datetime import datetime, timedelta

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model

from .models import *

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-input', 'placeholder': 'Логин'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-input', 'placeholder': 'Пароль'}))


class RegForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class CompetitionForm(forms.ModelForm):
    name = forms.CharField(label='Название', widget=forms.TextInput(attrs={'class':'form-input mb-6'}))
    date_begin = forms.DateField(label='Начало приема заявок', widget=forms.DateInput(attrs={'class':'form-input mb-6', 'type':'date'}))
    date_end = forms.DateField(label='Конец приема заявок', widget=forms.DateInput(attrs={'class':'form-input mb-6', 'type':'date'}))
    file = forms.FileField(required=False, label='Протокол', widget=forms.FileInput(attrs={'class':'form-input mb-6'}))
    comment = forms.CharField(required=False, label='Информация', widget=forms.Textarea(attrs={'class':'form-input mb-6'}))
    active = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-switch text-primary'}))
    cost = forms.IntegerField(label='Стоимость', widget=forms.NumberInput(attrs={'class':'form-input mb-6'}))
    type = forms.HiddenInput()

    class Meta:
        model = Event
        fields = ['name', 'date_begin', 'date_end', 'file', 'comment', 'active', 'cost', 'type']
        widgets = {
            'type':forms.HiddenInput(),
        }
    def __init__(self, *args, **kwargs):
        super(CompetitionForm, self).__init__(*args, **kwargs)
        self.fields['type'].required = False


class SeminarForm(forms.ModelForm):
    name = forms.CharField(label='Название', widget=forms.TextInput(attrs={'class':'form-input mb-6'}))
    date_begin = forms.DateField(label='Начало приема заявок', widget=forms.DateInput(attrs={'class':'form-input mb-6', 'type':'date'}))
    date_end = forms.DateField(label='Дата проведения', widget=forms.DateInput(attrs={'class':'form-input mb-6', 'type':'date'}))
    time_begin = forms.TimeField(label='Время начала', widget=forms.TimeInput(attrs={'class':'form-input mb-6', 'type':'time'}))
    time_end = forms.TimeField(label='Время окончания', widget=forms.TimeInput(attrs={'class':'form-input mb-6', 'type':'time'}))
    comment = forms.CharField(required=False, label='Комментарий', widget=forms.Textarea(attrs={'class':'form-input mb-6'}))
    active = forms.BooleanField(label='Активно', required=False,
                                widget=forms.CheckboxInput(attrs={'class':'form-switch text-primary'}))
    cost = forms.IntegerField(label='Стоимость', widget=forms.NumberInput(attrs={'class':'form-input mb-6'}))
    type = forms.HiddenInput()

    class Meta:
        model = Event
        fields = ['name', 'date_begin', 'date_end', 'time_begin','time_end', 'comment', 'cost', 'active', 'type']
        widgets = {
            'type':forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(SeminarForm, self).__init__(*args, **kwargs)
        self.fields['type'].required = False


class CompFormOrg(forms.ModelForm):
    fio = forms.CharField(label='ФИО спортсмена', widget=forms.TextInput(attrs={'class':'form-input mb-6'}))
    file = forms.FileField(label='Видео', widget=forms.FileInput(attrs={'class':'form-input mb-6'}))
    comment = forms.CharField(label='Комментарий', widget=forms.TextInput(attrs={'class':'form-input mb-6'}))
    event = forms.ModelChoiceField(queryset=Event.objects.filter(active=True, type='Соревнование'), label='Мероприятие',
                                   widget=forms.Select(attrs={'class': 'form-select mb-6'}))
    user = forms.HiddenInput()


    class Meta:
        model = AppCard
        fields = ['fio', 'event', 'comment', 'file', 'user']
        widgets = {
            'user': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(CompFormOrg, self).__init__(*args, **kwargs)
        self.fields['user'].required = False


class CompFormUser(forms.ModelForm):
    file = forms.FileField(label='Видео', widget=forms.FileInput(attrs={'class':'form-input mb-6'}))
    comment = forms.CharField(label='Комментарий', widget=forms.TextInput(attrs={'class':'form-input mb-6'}))
    event = forms.ModelChoiceField(queryset=Event.objects.filter(active=True, type = 'Соревнование'), label='Мероприятие',
                                   widget=forms.Select(attrs={'class':'form-select mb-6'}))
    anon = forms.BooleanField(required=False, label='Анонимно', widget=forms.CheckboxInput(attrs={'class':'form-switch text-primary'}))
    user = forms.HiddenInput()
    fio = forms.HiddenInput()


    class Meta:
        model = AppCard
        fields = ['event', 'comment', 'anon', 'file',  'user', 'fio']
        widgets = {
            'fio': forms.HiddenInput(),
            'user': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(CompFormUser, self).__init__(*args, **kwargs)
        self.fields['user'].required = False
        self.fields['fio'].required = False


class SeminarFormOrg(forms.ModelForm):
    fio = forms.CharField(label='ФИО спортсмена', widget=forms.TextInput(attrs={'class':'form-input mb-6'}))
    comment = forms.CharField(widget=forms.TextInput(attrs={'class':'form-input mb-6'}))
    event = forms.ModelChoiceField(queryset=Event.objects.filter(active=True, type='Семинар'), label='Мероприятие',
                                   widget=forms.Select(attrs={'class':'form-select mb-6'}))
    user = forms.HiddenInput()

    class Meta:
        model = AppCard
        fields = ['fio', 'comment', 'event', 'user']
        widgets = {
            'user': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(SeminarFormOrg, self).__init__(*args, **kwargs)
        self.fields['user'].required = False


class SeminarFormUser(forms.ModelForm):
    event = forms.ModelChoiceField(queryset=Event.objects.filter(active=True, type='Семинар'), label='Мероприятие',
                                   widget=forms.Select(attrs={'class':'form-select mb-6'}))
    comment = forms.CharField(label='Комментарий', widget=forms.TextInput(attrs={'class':'form-input mb-6'}))
    fio = forms.HiddenInput()
    user = forms.HiddenInput()

    class Meta:
        model = AppCard
        fields = [ 'event', 'comment', 'fio', 'user']
        widgets = {
            'fio': forms.HiddenInput(),
            'user': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(SeminarFormUser, self).__init__(*args, **kwargs)
        self.fields['user'].required = False
        self.fields['fio'].required = False


class SeminarAdminForm(forms.ModelForm):
    admin_comment = forms.CharField(label='Комментарий', widget=forms.TextInput(attrs={'class':'form-input mb-6'}))

    class Meta:
        model = AppCard
        fields = ['admin_comment']


class CompAdminForm(forms.ModelForm):
    score = forms.IntegerField(label='Баллы', widget=forms.NumberInput(attrs={'class':'form-input mb-6'}))
    admin_comment = forms.CharField(label='Комментарий', widget=forms.TextInput(attrs={'class':'form-input mb-6'}))

    class Meta:
        model = AppCard
        fields = ['score', 'admin_comment']


class NewsForm(forms.ModelForm):
    name = forms.CharField(label='Заголовок', widget=forms.TextInput(attrs={'class':'form-input mb-6'}))
    tag = forms.ModelChoiceField(queryset= Tag.objects.all(), label = 'Рубрика', widget=forms.Select(attrs={'class':'form-select mb-6'}))
    about = forms.CharField(required=True, label='Информация', widget=forms.Textarea(attrs={'class':'form-input mb-6'}))
    date_begin = forms.DateField(label='Начало приема заявок', widget=forms.DateInput(attrs={'class':'form-input mb-6', 'type':'date'}))
    date_end = forms.DateField(label='Дата проведения', widget=forms.DateInput(attrs={'class':'form-input mb-6', 'type':'date'}))
    time_begin = forms.TimeField(label='Время начала', widget=forms.TimeInput(attrs={'class':'form-input mb-6', 'type':'time'}))
    time_end = forms.TimeField(label='Время окончания', widget=forms.TimeInput(attrs={'class':'form-input mb-6', 'type':'time'}))
    active = forms.BooleanField(label='Активно', required=False,
                                widget=forms.CheckboxInput(attrs={'class':'form-switch text-primary'}))
    cost = forms.IntegerField(label='Стоимость', widget=forms.NumberInput(attrs={'class':'form-input mb-6'}))
    banner = forms.FileField(label='Баннер', widget=forms.FileInput(attrs={'class':'form-input mb-6'}))


    class Meta:
        model = News
        fields = '__all__'


class SeminarAdminComment(forms.Form):
    comment = forms.CharField(widget=forms.TextInput(attrs={'class':'form-input mb-6'}))


class ChangePassword(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].widget = forms.PasswordInput()
        self.fields["new_password1"].widget = forms.PasswordInput()
        self.fields["new_password2"].widget = forms.PasswordInput()

