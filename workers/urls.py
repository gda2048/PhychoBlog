from django.urls import path

from .views import PersonListView, AchievementListView, HelpItemListView, PersonDetailView


urlpatterns = [
                path('author/', PersonListView.as_view(), name='person_list'),
                path('achievement/', AchievementListView.as_view(), name='achievement_list'),
                path('help_item/', HelpItemListView.as_view(), name='help_item_list'),
                path(r'person/<int:pk>', PersonDetailView.as_view(), name='person'),
              ]
