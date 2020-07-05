import logging
from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist

from integrations.client import YoutubeVideoClient
from integrations.models import YoutubeCredentials
from videosearch.models import Setting
from videosearch.serializers import YoutubeVideoSerializer
logger = logging.getLogger(__name__)

# Defining Settings keys for querying Youtube Data API
FETCH_VIDEO_PUBLISHED_BEFORE_KEY = 'FETCH_VIDEO_PUBLISHED_BEFORE'
FETCH_VIDEO_PUBLISHED_AFTER_KEY = 'FETCH_VIDEO_PUBLISHED_AFTER'
FETCH_VIDEO_KEYWORDS_KEY = 'FETCH_VIDEO_KEYWORDS'
FETCH_VIDEO_MAX_RESULTS_KEY = 'FETCH_VIDEO_MAX_RESULTS'


def search_and_fetch_videos():
    """
    CRON Job which periodically fetches Videos from Youtube based on Setting provided and Stores in DB
    :return:
    """
    creds = YoutubeCredentials.active_objects.first()
    try:
        search_keywords = Setting.objects.get(key=FETCH_VIDEO_KEYWORDS_KEY).value
    except ObjectDoesNotExist:
        search_keywords = ''

    try:
        published_after = Setting.objects.get(key=FETCH_VIDEO_PUBLISHED_AFTER_KEY).value
    except ObjectDoesNotExist:
        published_after = '2020-06-01T00:00:00'

    try:
        max_results = Setting.objects.get(key=FETCH_VIDEO_MAX_RESULTS_KEY).value
    except ObjectDoesNotExist:
            max_results = 50

    _keywords = search_keywords.split(',')
    if int(max_results) > 50:
        _max_results = 50
    else:
        _max_results = int(max_results)
    _published_after = datetime.fromisoformat(published_after)

    youtube_client = YoutubeVideoClient(creds)
    response = youtube_client.fetch(
        keywords=_keywords,
        max_results=_max_results,
        order_by='date',
        published_after=_published_after)

    logger.info(f"Fetched {len(response)} Videos from Youtube")

    # Invoke Serializer for all Video
    for video_data in response:
        serializer = YoutubeVideoSerializer(data=video_data)
        try:
            if serializer.is_valid():
                serializer.save()
        except Exception as e:
            logger.exception(f"Failed to Serialize data due to {e}")

    # Updating the FETCH_VIDEO_PUBLISHED_AFTER_KEY value
    # Updates to the most recent date fetched
    last_response = response[0]
    Setting.objects.update_or_create(
        key=FETCH_VIDEO_PUBLISHED_AFTER_KEY,
        defaults={
            'value': datetime.isoformat(last_response.get('video_publish_date')),
        }
    )
    logger.info(f"Saved {len(response)} Videos to Database")

