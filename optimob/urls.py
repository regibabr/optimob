from django.contrib import admin
from django.urls import path
from optimob.views import home, sobre


urlpatterns = [
    
    path('', home),
    path('sobre/', sobre),
]