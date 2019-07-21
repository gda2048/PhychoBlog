from django.urls import path
from .views import ArticleListView, ArticleDetailView

urlpatterns = [
                path('article/', ArticleListView.as_view(), name='article_list'),
                path(r'article/<int:pk>', ArticleDetailView.as_view(), name='article'),
              ]
