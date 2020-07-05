import datetime

import pytz
from django.core.paginator import Paginator
from rest_framework import status, generics
from rest_framework.response import Response

from videosearch.serializers import YoutubeVideoDeserializer
from videosearch.helpers import (last_video_date,
                                 video_date_to_page_token)
from videosearch.models import YoutubeVideo

VIDEOS_PER_PAGE_SETTING_KEY = 2


class YoutubeVideosAPIView(generics.RetrieveAPIView):
    """
    Rest API view to Paginate data stored in DB
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.serializer_class = YoutubeVideoDeserializer

    def get(self, request, *args, **kwargs):
        epoch_start_datetime = datetime.datetime(year=1970, month=1, day=1, tzinfo=pytz.UTC)
        page_token = request.GET.get('PageToken', 1)

        try:
            page_last_video_epoch = last_video_date(page_token)
            assert page_last_video_epoch > 0
        except AttributeError:
            page_last_video_epoch = None
        except AssertionError:
            return Response(data={"PageToken": ["Invalid Page Token, Kindly enter correct Token"]},
                            status=status.HTTP_400_BAD_REQUEST)

        if page_last_video_epoch is not None:
            last_video_datetime = epoch_start_datetime + datetime.timedelta(seconds=page_last_video_epoch)
            videos = YoutubeVideo.objects.filter(video_publish_date__lt=last_video_datetime). \
                order_by('-video_publish_date')
        else:
            videos = YoutubeVideo.objects.order_by('-video_publish_date')

        # Invoke paginator to list all videos in pages
        paginator = Paginator(videos, VIDEOS_PER_PAGE_SETTING_KEY)
        paginated_videos_list = paginator.page(page_token).object_list
        serializer = self.serializer_class(paginated_videos_list, many=True)
        serializer_data = serializer.data

        new_last_video_epoch = (
                datetime.datetime.fromisoformat(serializer_data[len(serializer_data) - 1].get(
                    'video_publish_date')[:-1] + '+00:00') - epoch_start_datetime).total_seconds()
        next_page_token = video_date_to_page_token(int(new_last_video_epoch))
        data = {
            'next': next_page_token,
            'videos': serializer_data,
        }
        return Response(data=data, status=status.HTTP_200_OK)
