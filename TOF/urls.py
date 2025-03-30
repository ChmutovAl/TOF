"""
URL configuration for TOF project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import RedirectView
from tkd_online_forum.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('django.contrib.auth.urls')),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('login/', LoginUser.as_view(), name='login'),
    path('events/', EventsView.as_view(), name='events'),
    path('events/competitions', CompetitionsView.as_view(), name='competitions'),
    path('events/seminars', SeminarsView.as_view(), name='seminars'),
    path('app_cards', AppCardView.as_view(), name='app_cards'),
    path('competition_cards', CompCardView.as_view(), name='comp_cards'),
    path('seminar_cards', SeminarCardView.as_view(), name='sem_cards'),
    path('competitions/create', CompetitionsCreateView.as_view(), name='competitions_create'),
    path('seminars/create', SeminarsCreateView.as_view(), name='seminars_create'),
    path('app_cards/competitions/org/create', CompOrgView.as_view(), name='competitions_org_create'),
    path('app_cards/competitions/user/create', CompUserView.as_view(), name='competitions_user_create'),
    path('app_cards/seminars/org/create', SeminarOrgView.as_view(), name='seminars_org_create'),
    path('app_cards/seminars/user/create', SeminarUserView.as_view(), name='seminars_user_create'),
    path('events/<int:pk>', EventDetailView.as_view(), name='event_detail'),
    path('app_cards/<int:pk>', AppCardDetailView.as_view(), name='app_card_detail'),
    path('competitions/update/<int:pk>', CompetitionsUpdateView.as_view(), name='competitions_update'),
    path('seminars/update/<int:pk>', SeminarsUpdateView.as_view(), name='seminars_update'),
    path('app_cards/competitions/org/update/<int:pk>', CompOrgUpdateView.as_view(), name='competitions_org_update'),
    path('app_cards/competitions/user/update/<int:pk>', CompUserUpdateView.as_view(), name='competitions_user_update'),
    path('app_cards/seminars/org/update/<int:pk>', SeminarOrgUpdateView.as_view(), name='seminars_org_update'),
    path('app_cards/seminars/user/update/<int:pk>', SeminarUserUpdateView.as_view(), name='seminars_user_update'),
    path('events/delete/<int:pk>', EventDeleteView.as_view(), name='event_delete'),
    path('app_cards/delete/<int:pk>', AppCardDeleteView.as_view(), name='app_card_delete'),
    path('news/', NewsListView.as_view(), name='news'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('news/create', NewsCreateView.as_view(), name='news_create'),
    path('news/update/<int:pk>', NewsUpdateView.as_view(), name='news_update'),
    path('news/delete/<int:pk>', NewsDeleteView.as_view(), name='news_delete'),
    path('seminars/add_link/<int:pk>', seminar_link, name='seminar_link'),

    path('app_cards/competitions/evaluate', comp_value, name='comp_value'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
