from django.urls import path
from django.views.decorators.cache import cache_page


from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('article/', cache_page(60*15)(ArticleListView.as_view()), name='article_list'),
    path(r'article/<int:pk>', ArticleDetailView.as_view(), name='article'),
]
