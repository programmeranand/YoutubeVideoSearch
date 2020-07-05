from django.conf.urls import url

from videosearch.views import YoutubeVideosAPIView

app_name = 'videosearch'


urlpatterns = [
    url(r'^videos/$', YoutubeVideosAPIView.as_view(), name='video-list-view'),
]
