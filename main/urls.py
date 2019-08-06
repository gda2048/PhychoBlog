from django.urls import path

from .views import main, ProductListView

urlpatterns = [
    path('shop/', ProductListView.as_view(), name='shop'),
    path('main/', main, name='mains'),
]
