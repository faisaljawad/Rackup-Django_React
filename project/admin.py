from django.contrib import admin

# Register your models here.
from project.models import Project, Proposal

admin.site.register(Project)
admin.site.register(Proposal)