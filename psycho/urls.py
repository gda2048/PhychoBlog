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
from main import views
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .settings import site_name

admin.site.site_header = site_name
admin.site.site_title = site_name
admin.site.index_title = "Добро пожаловать"

urlpatterns = [
    path('author/', views.PersonListView.as_view(), name='person_list'),

    path('article/', views.ArticleListView.as_view(), name='article_list'),

    path('announcement/', views.AnnouncementListView.as_view(), name='announcement_list'),

    path('achievement/', views.AchievementListView.as_view(), name='achievement_list'),

    path('help_item/', views.HelpItemListView.as_view(), name='help_item_list'),
    path('event/', views.EventListView.as_view(), name='event_list'),

    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

