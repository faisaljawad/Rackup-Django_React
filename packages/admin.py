from django.contrib import admin

# Register your models here.
from packages.models import Package

admin.site.register(Package)