from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('navigate.urls')),
    path('', include('video.urls')),
    path('', include('postdetail.urls')),
    path('account/', include('account.urls')),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

