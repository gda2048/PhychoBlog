from django.urls import path
from .views import ArticleListView

urlpatterns = [
                  path('article/', ArticleListView.as_view(), name='article_list'),
              ]
