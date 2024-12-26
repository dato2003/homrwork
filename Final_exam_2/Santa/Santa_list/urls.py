from django.urls import path
from . import views

urlpatterns = [
    path('create_santas_list/', views.create_santas_list, name='create_santas_list'),
    path('view_santas_list/', views.view_santas_list, name='view_santas_list'),
    path('list_all_kids/', views.list_all_kids, name='list_all_kids'),
    path('kids/<int:id>/', views.view_kid, name='view_kid'),
    path('create_kid/', views.create_kid, name='create_kid'),
path('remove_kid/<int:kid_id>/', views.remove_kid_from_list, name='remove_kid_from_list'),
]

