import datetime
import email
from time import time
from django.db import models
from django.urls import reverse
##from embed_video.fields import EmbedVideoField
# Create your models here.
#Header section's classes are sequencially sorted in below's code
class Titles(models.Model):
    defaultname = models.CharField(max_length=200)


class BreakingNewsTitle(models.Model):
    defaultbreaking = models.CharField(max_length=300)

class BrowserIcon(models.Model):
    img = models.ImageField(upload_to='media/pics')


class Tricker(models.Model):
    name = models.CharField(max_length=500)
    url = models.URLField(null=True)

class StockReport(models.Model):
    
    currencyname = models.CharField(max_length=100)

    currencyvalue = models.FloatField(max_length=100)

    currencyminusindex = models.FloatField(max_length=100)

class Logo(models.Model):
    img = models.ImageField(upload_to='pics')
    url = models.URLField(null=True)

class HeaderAddvertise(models.Model):
    img = models.ImageField(upload_to='pics')
    url = models.URLField(null=True)
    

class NavItem(models.Model):
    liname = models.CharField(max_length=100)

class NavItemDropDown(models.Model):
    liname = models.CharField(max_length=100)


#Header section's classes are sequencially sorted in above's code



# All block content's including index.html is sorted below 


class SingleBlogPostContent(models.Model):
    bgimg = models.ImageField(upload_to='pics')
    tag = models.CharField(max_length=20)
    short_news = models.TextField(max_length=5000)
    date = models.DateField(auto_now_add=True)
    url = models.URLField(null=True)
    def __str__(self):
        return self.tag

    

class Marquee(models.Model):
    text = models.TextField(max_length=300)
    time = datetime.datetime.now()


class SinglePostTodayHeading(models.Model):
    heading = models.CharField(max_length=100)

#class ArticleDetailView(DetailView):

class BreakingNewsWidget(models.Model):
    widget_title = models.CharField(max_length=500)
    widgetimg = models.ImageField(upload_to='pics')
    widgetbreakingnewstitle = models.CharField(max_length=100)
    widgetheadline = models.CharField(max_length=100)

class DoNotMiss(models.Model):
    widget_title = models.CharField(max_length=200)
    post_thumbimg = models.ImageField(upload_to='pics')
    post_content = models.CharField(max_length=500)
    url = models.URLField(null=True)
    date = models.DateField(datetime.date)

class AddvertiseWidget(models.Model):
    widget_title = models.CharField(max_length=500)
    advert_thumb = models.ImageField(upload_to='pics')
    url = models.URLField(null=True)



class Subscribe(models.Model):
    heading = models.CharField(max_length=500)
    btnsubscribe = models.CharField(max_length=30)
    





## Editorial post Slider is also applicalble for category.html.

class EditorialPostSingleSlide(models.Model):
    img = models.ImageField(upload_to='pics')
    tag = models.CharField(max_length=100)
    url = models.URLField(null=True)
    headline = models.CharField(max_length=100)
    headlineafterbr = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
    para = models.CharField(max_length=2000)

## Editorial post Slider is also applicalble for category.html.

# All block content's including index.html is sorted above.

## Footer Section's classes are lied here

class FooterBgImg(models.Model):
    img = models.ImageField(upload_to='pics')


class FooterHeadlinea(models.Model):
    headline = models.CharField(max_length=100)

class FooterWidgetLista(models.Model):
    list = models.CharField(max_length=100)
    url = models.URLField(null=True)

class FooterHeadlineb(models.Model):
    headline = models.CharField(max_length=100)

class FooterWidgetListb(models.Model):
    list = models.CharField(max_length=100)
    url = models.URLField(null=True)

class FooterHeadlinec(models.Model):
    headline = models.CharField(max_length=100)

class FooterWidgetListc(models.Model):
    list = models.CharField(max_length=100)
    url = models.URLField(null=True)

class FooterHeadlined(models.Model):
    headline = models.CharField(max_length=100)

class FooterWidgetListd(models.Model):
    list = models.CharField(max_length=100)
    url = models.URLField(null=True)

class FooterHeadlinee(models.Model):
    headline = models.CharField(max_length=100)

class FooterWidgetListe(models.Model):
    list = models.CharField(max_length=100)
    url = models.URLField(null=True)

class FooterHeadlinef(models.Model):
    headline = models.CharField(max_length=100)

class FooterWidgetListf(models.Model):
    list = models.CharField(max_length=100)
    url = models.URLField(null=True)



# Category.html all models and object's are here.

class CategoryBreadcumbArea(models.Model):
    tag = models.CharField(max_length=300)
    date = models.DateField(datetime.date)
    url = models.URLField(null=True)


class CatagoryGazetteWelcomePostAreaa(models.Model):
    gazetteposttag = models.CharField(max_length=300)
    gazettepostheadline = models.CharField(max_length=300)
    gazettepostdate = models.DateField(auto_now_add=True)
    gazettepostimg = models.ImageField(upload_to='pics')
    gazettepostparagraph = models.TextField(max_length=2000)
    gazettepostbtn =models.CharField(max_length=200)
    url = models.URLField(null=True)

class CatagoryGazetteWelcomePostAreab(models.Model):
    gazetteposttag = models.CharField(max_length=300)
    gazettepostheadline = models.CharField(max_length=300)
    gazettepostdate = models.DateField(auto_now_add=True)
    gazettepostimg = models.ImageField(upload_to='pics')
    gazettepostparagraph = models.TextField(max_length=2000)
    gazettepostbtn = models.CharField(max_length=200)
    url = models.URLField(null=True)

class CatagoryGazetteWelcomePostAreac(models.Model):

    gazetteposttag = models.CharField(max_length=300)
    gazettepostheadline = models.CharField(max_length=300)
    gazettepostdate = models.DateField(auto_now_add=True)
    gazettepostimg = models.ImageField(upload_to='pics')
    gazettepostparagraph = models.TextField(max_length=2000)
    gazettepostbtn =models.CharField(max_length=200)
    url = models.URLField(null=True)
    
class PaginationListItem(models.Model):

    url = models.URLField()
    num = models.IntegerField()

class PaginationListNextButton(models.Model):
    url = models.URLField(null=True)
    num = models.CharField(max_length=5)

# Category.html all models and object's are here.


#Aboyt-Us area.
class AboutUsBreadcumbArea(models.Model):

    heading = models.CharField(max_length=500)
    date = models.DateField(datetime.date)

class GazetteAboutUsArea(models.Model):

    heading = models.CharField(max_length=500)
    paragraph1 = models.TextField(max_length=3000)
    paragraph2 = models.TextField(max_length=3000)

class TeamArea(models.Model):
    heading = models.CharField(max_length=300)

class SingleTeamArea(models.Model):

    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=300)
    role = models.CharField(max_length=3000)
    detail = models.TextField(max_length=2000)
    sociallinks = models.URLField()

class SocialLink(models.Model):
    href = models.URLField(max_length=100)
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.href
        
class GazetteCtaArea(models.Model):
    image = models.ImageField(upload_to='pics')
    heading = models.CharField(max_length=1000)
    paragraph = models.TextField(max_length=5000)
    
    def __str__(self):
        return self.heading

# Contact.html all models and object's are here...


class ContactUsBreadcumbArea(models.Model):

    heading = models.CharField(max_length=500)
    date = models.DateField(datetime.date)

class GazetteContactArea(models.Model):

    heading = models.CharField(max_length=300)
    formtext = models.TextField(max_length=5000)
    formemail = models.EmailField(max_length=30)
    formmsg = models.TextField(max_length=5000)
    formbtn = models.CharField(max_length=300)

class ContactAddressInfo(models.Model):
    heading = models.CharField(max_length=500)
    infopara1 = models.CharField(max_length=500)
    infopara2 = models.CharField(max_length=500)
    infopara3 = models.CharField(max_length=500)
    phoneheading = models.CharField(max_length=500)
    contactinfo1 = models.CharField(max_length=500)
    contactinfo2 = models.CharField(max_length=500)
    contactinfo3 = models.CharField(max_length=500)

# Single Post .HTML pages Class and Objects

class SinglePostArea(models.Model):
    img = models.ImageField(upload_to='pics')
    tag = models.CharField(max_length=1000)
    url = models.URLField(null=True)
    heading = models.CharField(max_length=1000)
    date = models.DateField(datetime.date)
    

class SinglePostAreaContents(models.Model):
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    p3 = models.CharField(max_length=1000)
    imgthumb = models.ImageField(upload_to='pics')
    ptext1 = models.CharField(max_length=1000)
    ptext2 = models.CharField(max_length=1000)
    blockqts = models.CharField(max_length=1000)
    singleptxt = models.TextField(max_length=1000)
    

class SinglePostDiscussionArea(models.Model):
    heading = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pics')
    commentperson = models.CharField(max_length=200)
    commentdate = models.DateField(datetime.date)
    commenttext = models.TextField(max_length=1000)
    replybtn = models.CharField(max_length=200)


class LeaveCommentArea(models.Model):
    heading = models.CharField(max_length=1000)
    formtext = models.CharField(max_length=1000)
    formemail = models.EmailField(max_length=30, null=True)
    formmsg = models.TextField(max_length=2500)
    formbtn = models.CharField(max_length=20, null=True)



####Search Pages Necessary Contents
class SearchArea(models.Model):
    searchposttag = models.CharField(max_length=300)
    searchpostheadline = models.CharField(max_length=300)
    searchpostdate = models.DateField(auto_now_add=True)
    searchpostimg = models.ImageField(upload_to='pics')
    searchpostparagraph = models.TextField(max_length=5000)
    searchpostbtn =models.CharField(max_length=20)
    searchurl = models.URLField(null=True)


class SportNewsArea(models.Model):
    img = models.ImageField(upload_to='pics')
    tag = models.CharField(max_length=1000)
    url = models.URLField(null=True)
    heading = models.CharField(max_length=1000)
    date = models.DateField(datetime.date)



class SportNews(models.Model):
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    p3 = models.CharField(max_length=1000)
    imgthumb = models.ImageField(upload_to='pics')
    ptext1 = models.CharField(max_length=1000)
    ptext2 = models.CharField(max_length=1000)
    blockqts = models.CharField(max_length=1000)
    singleptxt = models.TextField(max_length=1000)



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