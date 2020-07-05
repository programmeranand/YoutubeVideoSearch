from datetime import datetime

from rest_framework import serializers
from rest_framework.fields import empty

from videosearch.models import YoutubeVideo


class YoutubeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeVideo
        fields = '__all__'

    def __init__(self, data=empty, *args, **kwargs):
        data['video_publish_date'] = datetime.fromtimestamp(data.get('video_publish_date'))
        super().__init__(data=data, *args, **kwargs)


class YoutubeVideoDeserializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeVideo
        fields = '__all__'
