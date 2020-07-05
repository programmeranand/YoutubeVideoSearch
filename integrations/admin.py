from django.contrib import admin

from integrations.models import YoutubeCredentials


@admin.register(YoutubeCredentials)
class YoutubeCredentialsAdmin(admin.ModelAdmin):
    pass
