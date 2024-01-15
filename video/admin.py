from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin
# Register your models here.


class NewsModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(NewsStream, NewsModelAdmin)
