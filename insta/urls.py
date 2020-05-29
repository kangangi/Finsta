from django.conf import settings
from django.conf.urls.static import static

urlpattern = []

if settings.DEBUG:
    urlpattern+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)