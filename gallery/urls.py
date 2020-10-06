from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('add/', views.add_entry, name='add_entry'),
    path('edit/<entry_number>/', views.edit_entry, name='edit_entry'),
    path('delete/<entry_number>/', views.delete_entry, name='delete_entry'),
]
