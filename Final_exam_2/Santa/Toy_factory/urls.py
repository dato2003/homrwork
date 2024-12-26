from django.urls import path
from . import views

urlpatterns = [
    path('create_toy/', views.create_toy, name='create_toy'),
    path('toy/<int:kid_id>/', views.view_toy, name='view_toy'),
    path('generate_gift', views.generate_gift, name='generate_gift'),
    path('view_all_toys/', views.view_all_toys, name='view_all_toys'),
]
