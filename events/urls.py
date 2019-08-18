from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import AnnouncementListView, EventListView, EventDetailView

urlpatterns = [
    path('', cache_page(60 * 15)(AnnouncementListView.as_view()), name='announcement_list'),
    re_path('^(?P<type>[a-zA-Z0-9-]+)/$', cache_page(60 * 15)(EventListView.as_view()), name='event_list'),
    path(r'event/<int:pk>/', EventDetailView.as_view(), name='event'),
]
