import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from blog.models import ArticlePhotoReport
from events.models import Event
from shop.models import Product
from workers.models import Achievement, Person
from .settings import site_name

if not os.path.exists(settings.MEDIA_ROOT):
    os.makedirs(settings.MEDIA_ROOT)

ArticlePhotoReport.all_img_from_binary()
Achievement.all_img_from_binary()
Event.all_img_from_binary()
Person.all_img_from_binary()
Product.all_img_from_binary()

admin.site.site_header = site_name
admin.site.site_title = site_name
admin.site.index_title = "Добро пожаловать в панель настроек " + site_name

urlpatterns = [
                  path('blog/', include('blog.urls')),
                  path('workers/', include('workers.urls')),
                  path('mail/', include('mail.urls')),
                  path('shop/', include('shop.urls')),
                  path('summernote/', include('django_summernote.urls')),
                  path('admin/', admin.site.urls),
                  path('', include('events.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
