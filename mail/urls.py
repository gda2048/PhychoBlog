from django.urls import path

from .views import ContactView

urlpatterns = [
    path('form/', ContactView.as_view(), name='contact_form'),
]
