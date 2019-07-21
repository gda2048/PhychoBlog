from django.urls import path, re_path

from .views import AnnouncementListView, EventListView, EventDetailView

urlpatterns = [
                path('announcement/', AnnouncementListView.as_view(), name='announcement_list'),
                re_path('^events/(?P<type>[a-zA-Z0-9-]+)/$', EventListView.as_view(), name='event_list'),
                path(r'event/<int:pk>/', EventDetailView.as_view(), name='event'),
              ]
