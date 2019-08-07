from django.urls import path
from shop.views import ProductListView

urlpatterns = [
    path('/', ProductListView.as_view(), name='shop')
]
