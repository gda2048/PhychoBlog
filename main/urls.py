from django.urls import path

from .views import main, shop

urlpatterns = [
                path('shop/', shop, name='shop'),
                path('main/', main, name='mains'),
              ]
