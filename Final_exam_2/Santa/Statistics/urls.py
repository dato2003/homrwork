# Statistics/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('nice_naughty_statistics/', views.nice_naughty_statistics, name='nice_naughty_statistics'),
    path('toy_statistics/', views.toy_statistics, name='toy_statistics'),
    path('toy_creation_time/', views.toy_creation_time, name='toy_creation_time'),
    path('delivery_time/', views.delivery_time, name='delivery_time'),
]
