import datetime
import logging

from youtube_api import YouTubeDataAPI

from integrations.models import YoutubeCredentials

KEY_YOUTUBE_PUBLISHED_DATE = 'YOUTUBE_PUBLISHED_DATE'

logger = logging.getLogger(__name__)


class YoutubeVideoClient:
    """
    Youtube Client to query using Youtube Data API
    """
    def __init__(self, api_credentials: YoutubeCredentials):
        self.credentials = api_credentials

    def fetch(self, keywords, published_after=None, published_before=None, max_results=5, order_by='date'):
        yt = YouTubeDataAPI(self.credentials.api_key)
        if published_after:
            _published_after = published_after.date()
        else:
            _published_after = datetime.datetime.timestamp(datetime.datetime(2000, 1, 1))
        if published_before:
            _published_before = published_before.date()
        else:
            _published_before = datetime.datetime.timestamp(datetime.datetime(3000, 1, 1))
        response = yt.search(
            keywords,
            max_results=max_results,
            order_by=order_by,
            published_after=_published_after,
            published_before=_published_before,
        )
        logger.info(f"Fetching videos from Youtube : {response}")

        return response
