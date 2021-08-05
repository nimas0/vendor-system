from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from .views import PhotographerViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('photographers', PhotographerViewSet, basename='photographers')
router.register('users', UserViewSet)


urlpatterns = [

    path('api/', include(router.urls))

    #path('photographers/', PhotographerList.as_view()),
    #path('photographers/<int:vendor_id>/', PhotographerDetails.as_view())
    # path('photographers/', photographer_list),
    # path('photographers/<int:pk>/', photographer_details)
]