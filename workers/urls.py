from django.urls import path
from django.views.decorators.cache import cache_page
from .views import PersonListView, HelpItemListView, PersonDetailView, AchievementDetailView


urlpatterns = [
    path('expert/', cache_page(60*15)(PersonListView.as_view()), name='person_list'),
    path(r'achievement/<int:pk>', cache_page(60*15)(AchievementDetailView.as_view()), name='achievement'),
    path('help_item/', cache_page(60*15)(HelpItemListView.as_view()), name='help_item_list'),
    path(r'person/<int:pk>', cache_page(60*15)(PersonDetailView.as_view()), name='person'),
]
