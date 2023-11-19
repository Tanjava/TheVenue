from .import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('reservations/', views.reservations, name='reservations')
]