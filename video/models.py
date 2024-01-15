from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.

class NewsStream(models.Model):
    url = EmbedVideoField()
    btn = models.CharField(max_length=30)
    tag = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    added = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    def __str__(self):
        return self.url


