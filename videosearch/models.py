from django.db import models

# Create your models here.


class BaseModel(models.Model):
    """
    This will add the basic fields to the model
    """

    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class YoutubeVideo(BaseModel):
    """
    Stores Video Related details
    """
    channel_id = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        db_index=True
    )
    channel_title = models.CharField(
        max_length=400,
        blank=True,
        null=True,
    )

    video_id = models.CharField(
        max_length=30,
        unique=True,
        null=False,
        db_index=True
    )
    video_title = models.CharField(
        max_length=300,
        blank=True,
        null=True
    )
    video_description = models.TextField(null=True, blank=True)
    video_thumbnail = models.URLField(blank=True, null=True)
    video_publish_date = models.DateTimeField()


class Setting(BaseModel):
    key = models.CharField(max_length=128, unique=True)
    value = models.CharField(max_length=512, default='', blank=True)

    def __str__(self):
        return self.key
