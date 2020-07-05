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
        self.published_before = None
        self.published_after = datetime.datetime.timestamp(datetime.datetime(2018, 1, 1))
        self.published_before = datetime.datetime.timestamp(datetime.datetime(2021, 1, 1))

    def fetch_videos(self, keywords,
                     published_after=None,
                     published_before=None,
                     max_results=5,
                     order_by='date'):
        youtube_search = YouTubeDataAPI(self.credentials.api_key)
        if published_after:
            self.published_after = published_after.date()

        if published_before:
            self.published_before = published_before.date()

        response = youtube_search.search(
            keywords,
            max_results=max_results,
            order_by=order_by,
            published_after=self.published_after,
            published_before=self.published_before,
        )
        logger.info(f"Fetching videos from Youtube : {response}")

        return response
