from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='inicio-home'),
    path('about/', views.about, name='about-home'),
    path('practica/', views.practica, name='practica-home')
    
]