"""psycho URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import RedirectView

import blog.views as blog_view
import events.views as event_view
import main.views as main_view
import workers.views as workers_view
from .settings import site_name

admin.site.site_header = site_name
admin.site.site_title = site_name
admin.site.index_title = "Добро пожаловать"

urlpatterns = [
                  path('author/', workers_view.PersonListView.as_view(), name='person_list'),

                  path('article/', blog_view.ArticleListView.as_view(), name='article_list'),

                  path('announcement/', event_view.AnnouncementListView.as_view(), name='announcement_list'),

                  path('achievement/', workers_view.AchievementListView.as_view(), name='achievement_list'),

                  path('help_item/', workers_view.HelpItemListView.as_view(), name='help_item_list'),

                  path('admin/', admin.site.urls),
                  path('', main_view.main, name='main'),
                  path('shop/', main_view.shop, name='shop'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    re_path('^event/(?P<type>[a-zA-Z0-9-]+)/$', event_view.EventListView.as_view(), name='event_list'),
]
