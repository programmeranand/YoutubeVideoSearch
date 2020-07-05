from django.contrib import admin

from videosearch.models import Setting, YoutubeVideo


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('key', 'value', 'modified')
    search_fields = ('key', 'value')
    list_filter = ('modified',)
    ordering = ['key']


@admin.register(YoutubeVideo)
class YoutubeVideoAdmin(admin.ModelAdmin):
    pass
