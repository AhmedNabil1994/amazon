
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from pages.models import Myusers
from .views import Userslist
from myapi import views


router = routers.DefaultRouter()
router.register(r'Myusers',Userslist)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('Myusers/<int:pk>/',
         views.usersOperations,
         name = 'employee-detail'),




]

