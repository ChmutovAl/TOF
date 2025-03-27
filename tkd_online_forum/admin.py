from django.contrib import admin

from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'mid_name']
    search_fields = ['last_name', 'first_name', 'mid_name']


class EventAdmin(admin.ModelAdmin):
    list_display = ['type', 'name', 'date_begin', 'date_end', 'active']
    search_fields = ['type', 'name', 'date_begin', 'date_end', 'active']


class AppCardAdmin(admin.ModelAdmin):
    list_display = ['fio', 'event', 'score', 'anon', 'status', 'file']
    search_fields = ['fio', 'score', 'anon', 'status', 'file']


class FederationAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class BeltAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class QualificationAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class NewsAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(User, UserAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(AppCard, AppCardAdmin)
admin.site.register(Federation, FederationAdmin)
admin.site.register(Belt, BeltAdmin)
admin.site.register(Qualification, QualificationAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Tag, TagAdmin)