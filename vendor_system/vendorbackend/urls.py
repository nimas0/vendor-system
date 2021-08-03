from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from .views import photographer_list, photographer_details

urlpatterns = [
    path('photographers/', photographer_list),
    path('photographers/<int:pk>/', photographer_details)
]