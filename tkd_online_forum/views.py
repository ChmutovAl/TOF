from datetime import datetime, timedelta


from django.db.models import Count
from django.contrib.auth import update_session_auth_hash
from django.forms import formset_factory, modelformset_factory
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, ListView, CreateView, DeleteView, FormView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *
from django.core.paginator import Paginator

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'


class SignUpView(CreateView):
    form_class = RegForm
    success_url = reverse_lazy('login')
    template_name = 'registration.html'


    def form_valid(self, form):
        self.form = form.save(commit=False)
        self.form.save()
        return super().form_valid(form)


class EventsView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'events.html'

    def get_queryset(self):
        if self.request.user.admin:
            return Event.objects.all()
        return Event.objects.filter(active=True)


class CompetitionsView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'competitions.html'

    def get_queryset(self):
        if self.request.user.admin:
            return Event.objects.filter(type = 'Соревнование')
        return Event.objects.filter(active=True, type = 'Соревнование')

class SeminarsView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'seminars.html'

    def get_queryset(self):
        if self.request.user.admin:
            return Event.objects.filter(type = 'Семинар')
        return Event.objects.filter(active=True, type = 'Семинар')


class AppCardView(LoginRequiredMixin, ListView):
    model = AppCard
    template_name = 'app_cards.html'

    def get_queryset(self):
        if self.request.user.admin:
            return AppCard.objects.filter(status=True)
        return AppCard.objects.filter(user=self.request.user)


class CompCardView(LoginRequiredMixin, ListView):
    model = AppCard
    template_name = 'comp_cards.html'

    def get_queryset(self):
        if self.request.user.admin:
            return AppCard.objects.filter(status=True, event__type='Соревнование')
        return AppCard.objects.filter(user=self.request.user, event__type='Соревнование')


class SeminarCardView(LoginRequiredMixin, ListView):
    model = AppCard
    template_name = 'sem_cards.html'

    def get_queryset(self):
        if self.request.user.admin:
            return AppCard.objects.filter(status=True, event__type='Семинар')
        return AppCard.objects.filter(user=self.request.user, event__type='Семинар')


class CompetitionsCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = CompetitionForm
    template_name = 'form.html'
    success_url = reverse_lazy('competitions')

    def form_valid(self, form):
        comp_form = form.save(commit=False)
        comp_form.type = 'Соревнование'
        comp_form.save()
        return super().form_valid(form)


class SeminarsCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = SeminarForm
    template_name = 'form.html'
    success_url = reverse_lazy('seminars')

    def form_valid(self, form):
        sem_form = form.save(commit=False)
        sem_form.type = 'Семинар'
        sem_form.save()
        return super().form_valid(form)


class CompOrgView(LoginRequiredMixin, CreateView):
    model = AppCard
    form_class = CompFormOrg
    template_name = 'form.html'
    success_url = reverse_lazy('comp_cards')

    def form_valid(self, form):
        comp_form = form.save(commit=False)
        comp_form.user = self.request.user
        comp_form.save()
        return super().form_valid(form)


class CompUserView(LoginRequiredMixin, CreateView):
    model = AppCard
    form_class = CompFormUser
    template_name = 'form.html'
    success_url = reverse_lazy('comp_cards')

    def form_valid(self, form):
        comp_form = form.save(commit=False)
        if not comp_form.anon:
            comp_form.fio = (self.request.user.last_name + ' ' + self.request.user.mid_name  + ' ' +
                             self.request.user.first_name  + ' ')
        else:
            comp_form.fio = self.request.user.username
        comp_form.user = self.request.user
        return  super().form_valid(form)


class SeminarOrgView(LoginRequiredMixin, CreateView):
    model = AppCard
    form_class = SeminarFormOrg
    template_name = 'form.html'
    success_url = reverse_lazy('sem_cards')

    def form_valid(self, form):
        sem_form = form.save(commit=False)
        sem_form.user = self.request.user
        sem_form.save()
        return super().form_valid(form)


class SeminarUserView(LoginRequiredMixin, CreateView):
    model = AppCard
    form_class = SeminarFormUser
    template_name = 'form.html'
    success_url = reverse_lazy('sem_cards')

    def form_valid(self, form):
        sem_form = form.save(commit=False)
        sem_form.user = self.request.user
        sem_form.fio = (self.request.user.last_name + ' ' + self.request.user.mid_name + ' ' +
                        self.request.user.first_name + ' ')
        sem_form.save()
        return super().form_valid(form)


class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = 'event_detail.html'


class AppCardDetailView(LoginRequiredMixin, DetailView):
    model = AppCard
    template_name = 'app_card_detail.html'


class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = 'events.html'
    success_url = reverse_lazy('events')


class AppCardDeleteView(LoginRequiredMixin, DeleteView):
    model = AppCard
    template_name = 'app_cards.html'
    success_url = reverse_lazy('app_cards')

    def get_object(self, queryset=None):
        return AppCard.objects.get(id=self.kwargs['pk'])


class CompetitionsUpdateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = CompetitionForm
    template_name = 'form.html'
    success_url = reverse_lazy('competitions')



class SeminarsUpdateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = SeminarForm
    template_name = 'form.html'
    success_url = reverse_lazy('seminars')



class CompOrgUpdateView(LoginRequiredMixin, CreateView):
    model = AppCard
    form_class = CompFormOrg
    template_name = 'form.html'
    success_url = reverse_lazy('comp_cards')



class CompUserUpdateView(LoginRequiredMixin, CreateView):
    model = AppCard
    form_class = CompFormUser
    template_name = 'form.html'
    success_url = reverse_lazy('comp_cards')



class SeminarOrgUpdateView(LoginRequiredMixin, CreateView):
    model = AppCard
    form_class = SeminarFormOrg
    template_name = 'form.html'
    success_url = reverse_lazy('sem_cards')



class SeminarUserUpdateView(LoginRequiredMixin, CreateView):
    model = AppCard
    form_class = SeminarFormUser
    template_name = 'form.html'
    success_url = reverse_lazy('sem_cards')
