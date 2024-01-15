import datetime
from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.

class DetailPostHeading(models.Model):
    heading = models.CharField(max_length=100)
    
class SinglePostToday(models.Model):

    post_thumb_img = models.ImageField(upload_to='pics')
    tag = models.CharField(max_length=30)
    headline = models.CharField(max_length=100)
    date = models.DateField(datetime.date)
    comment = models.CharField(max_length=100)
    para = models.CharField(max_length=5000)

    def __str__(self) -> str:
        return self.headline


class BreakingNewsWidget(models.Model):

    widget_title = models.CharField(max_length=50)
    widgetimg = models.ImageField(upload_to='pics')
    widgetbreakingnewstitle = models.CharField(max_length=100)
    widgetheadline = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.widgetheadline



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


class GazetteCtaArea(models.Model):
    image = models.ImageField(upload_to='pics')
    heading = models.CharField(max_length=100)
    paragraph = models.TextField(max_length=500)
    
    def __str__(self):
        return self.heading



class TeamArea(models.Model):
    heading = models.CharField(max_length=30)

class SingleTeamArea(models.Model):
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    detail = models.TextField(max_length=2000)
    sociallinks = models.URLField()

class SocialLink(models.Model):
    href = models.URLField(max_length=100)
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.href
    


class EditorialPostSingleSlide(models.Model):
    img = models.ImageField(upload_to='pics')
    tag = models.CharField(max_length=20)
    url = models.URLField(null=True)
    headline = models.CharField(max_length=50)
    headlineafterbr = models.CharField(max_length=150)
    date = models.DateField(auto_now_add=True)
    para = models.CharField(max_length=2000)


class CatagoryGazetteWelcomePostAreaa(models.Model):
    gazetteposttag = models.CharField(max_length=30)
    gazettepostheadline = models.CharField(max_length=30)
    gazettepostdate = models.DateField(auto_now_add=True)
    gazettepostimg = models.ImageField(upload_to='pics')
    gazettepostparagraph = models.TextField(max_length=2000)
    gazettepostbtn =models.CharField(max_length=20)
    url = models.URLField(null=True)

class CatagoryGazetteWelcomePostAreab(models.Model):
    gazetteposttag = models.CharField(max_length=30)
    gazettepostheadline = models.CharField(max_length=30)
    gazettepostdate = models.DateField(auto_now_add=True)
    gazettepostimg = models.ImageField(upload_to='pics')
    gazettepostparagraph = models.TextField(max_length=2000)
    gazettepostbtn = models.CharField(max_length=20)
    url = models.URLField(null=True)

class CatagoryGazetteWelcomePostAreac(models.Model):

    gazetteposttag = models.CharField(max_length=30)
    gazettepostheadline = models.CharField(max_length=30)
    gazettepostdate = models.DateField(auto_now_add=True)
    gazettepostimg = models.ImageField(upload_to='pics')
    gazettepostparagraph = models.TextField(max_length=2000)
    gazettepostbtn =models.CharField(max_length=20)
    url = models.URLField(null=True)


class CulturalNewsArea(models.Model):
    img = models.ImageField(upload_to='pics')
    tag = models.CharField(max_length=1000)
    url = models.URLField(null=True)
    heading = models.CharField(max_length=1000)
    date = models.DateField(datetime.date)

class CulturalNews(models.Model):
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    p3 = models.CharField(max_length=1000)
    imgthumb = models.ImageField(upload_to='pics')
    ptext1 = models.CharField(max_length=1000)
    ptext2 = models.CharField(max_length=1000)
    blockqts = models.CharField(max_length=1000)
    singleptxt = models.TextField(max_length=1000)