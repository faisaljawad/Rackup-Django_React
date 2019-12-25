from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('viewProjects', projectList.as_view(), name='viewProjects'),
    path('viewProposals', proposalList.as_view(), name='viewProposals'),
]
