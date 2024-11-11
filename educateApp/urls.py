from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='my_home'),
    path('about/', views.about, name='my_about'),
    path('services/', views.services, name='my_services'),
]
