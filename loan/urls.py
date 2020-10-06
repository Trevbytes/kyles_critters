from django.urls import path
from . import views

urlpatterns = [
    path('', views.loan, name='loan'),
    path('request_success/<order_number>/',
         views.request_success, name='request_success')
]