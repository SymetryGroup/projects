from django.urls import path
from .import views

urlpatterns=[

     path('languages/',views.ruso,name='ruso-home')

]
