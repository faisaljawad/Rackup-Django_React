from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('viewUsers', userList.as_view(), name='viewUser'),
    path('viewCertifications', certificationList.as_view(), name='viewCertifications'),
    path('viewSkills', skillsList.as_view(), name='viewSkills'),
    path('viewProfiles', profileList.as_view(), name='viewProfiles'),
    path('viewReviews', reviewsList.as_view(), name='viewReviews'),
    path('viewAccounts', accountList.as_view(), name='viewAccounts'),
]
