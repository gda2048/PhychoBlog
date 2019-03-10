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

urlpatterns = [
    path('author/create/', views.PersonCreate.as_view(), name='person_create'),
    path('author/update/<int:pk>/', views.PersonUpdate.as_view(), name='person_update'),
    path('author/delete/<int:pk>/', views.PersonDelete.as_view(), name='person_delete'),
    re_path(r'author/', views.PersonListView.as_view(), name='person_list'),

    path('article/', views.ArticleListView.as_view(), name='article_list'),
    path('article/create/', views.ArticleCreate.as_view(), name='article_create'),
    path('article/update/<int:pk>/', views.ArticleUpdate.as_view(), name='article_update'),
    path('article/delete/<int:pk>/', views.ArticleDelete.as_view(), name='article_delete'),

    path('announcement/', views.AnnouncementListView.as_view(), name='announcement_list'),
    path('announcement/create/', views.AnnouncementCreate.as_view(), name='announcement_create'),
    path('announcement/update/<int:pk>/', views.AnnouncementUpdate.as_view(), name='announcement_update'),
    path('announcement/delete/<int:pk>/', views.AnnouncementDelete.as_view(), name='announcement_delete'),

    path('achievement/', views.AchievementListView.as_view(), name='achievement_list'),
    path('achievement/create/', views.AchievementCreate.as_view(), name='achievement_create'),
    path('achievement/update/<int:pk>/', views.AchievementUpdate.as_view(), name='achievement_update'),
    path('achievement/delete/<int:pk>/', views.AchievementDelete.as_view(), name='achievement_delete'),

    path('help_item/', views.HelpItemListView.as_view(), name='help_item_list'),
    path('help_item/create/', views.HelpItemCreate.as_view(), name='help_item_create'),
    path('help_item/update/<int:pk>/', views.HelpItemUpdate.as_view(), name='help_item_update'),
    path('help_item/delete/<int:pk>/', views.HelpItemDelete.as_view(), name='help_item_delete'),

    path('', views.main, name='main'),
]
