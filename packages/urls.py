from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('viewPackages', packagesList.as_view(), name='viewPackages'),
]
