import os
from django.contrib import admin
from .models import Url


@admin.register(Url)
class UrlsAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'check', 'status')
    list_display_links = ('url',)
    ordering = ('id',)
    list_editable = ['check']
