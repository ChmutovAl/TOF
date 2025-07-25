from datetime import datetime, timedelta
from lib2to3.fixes.fix_input import context

from django.db.models import Count
from django.contrib.auth import update_session_auth_hash
from django.forms import formset_factory, modelformset_factory
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse, HttpResponseRedirect
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


class CompetitionsUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = CompetitionForm
    template_name = 'form.html'
    success_url = reverse_lazy('competitions')


class SeminarsUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = SeminarForm
    template_name = 'form.html'
    success_url = reverse_lazy('seminars')


class CompOrgUpdateView(LoginRequiredMixin, UpdateView):
    model = AppCard
    form_class = CompFormOrg
    template_name = 'form.html'
    success_url = reverse_lazy('comp_cards')


class CompUserUpdateView(LoginRequiredMixin, UpdateView):
    model = AppCard
    form_class = CompFormUser
    template_name = 'form.html'
    success_url = reverse_lazy('comp_cards')


class SeminarOrgUpdateView(LoginRequiredMixin, UpdateView):
    model = AppCard
    form_class = SeminarFormOrg
    template_name = 'form.html'
    success_url = reverse_lazy('sem_cards')


class SeminarUserUpdateView(LoginRequiredMixin, UpdateView):
    model = AppCard
    form_class = SeminarFormUser
    template_name = 'form.html'
    success_url = reverse_lazy('sem_cards')


class NewsListView(LoginRequiredMixin, ListView):
    model = News
    template_name = 'news.html'

    def get_queryset(self):
        if self.request.user.admin:
            return News.objects.all()
        return News.objects.filter(active=True)


class NewsDetailView(LoginRequiredMixin, DetailView):
    model = News
    template_name = "new.html"


class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    form_class = NewsForm
    template_name = "form.html"
    success_url = reverse_lazy('news')


class NewsUpdateView(LoginRequiredMixin, UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'form.html'
    success_url = reverse_lazy('news')


class NewsDeleteView(LoginRequiredMixin, DeleteView):
    model = News
    template_name = 'news.html'
    success_url = reverse_lazy('news')

    def get_object(self, queryset=None):
        return News.objects.get(id=self.kwargs['pk'])

def seminar_link(request, pk):
    if request.method == 'POST':
        form = SeminarLink(request.POST)
        if form.is_valid():
            AppCard.objects.filter(event_id=pk).update(admin_comment=form.cleaned_data['comment'])
            return HttpResponseRedirect(reverse('seminars'))
    return render(request, 'form.html', {'form': form})


def comp_value(request):
    context={}
    list = AppCard.objects.filter(event__type='Соревнования', status=True)[:10]
    comp_formset = modelformset_factory(model=AppCard, form=CompAdminForm, extra=0)
    if request.method == 'POST':
        formset = comp_formset(request.POST or None, request.FILES or None, initial=list)
        if formset.is_valid():
            print(formset.cleaned_data)
            instances = formset.save(commit=False)
            for instance in instances:
                print(instance)
                instance.save()
            return redirect('comp_value')
        else:
            print(formset.errors)
    else:
        formset = comp_formset(queryset=list)
    context['formset'] = formset
    print(formset.is_valid())
    return render(request, "comp_cards_admin.html", context)


def event_change_active(request, pk):
    event = Event.objects.get(id=pk)
    if event.active:
        event.active = False
    else:
        event.active = True
    event.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))