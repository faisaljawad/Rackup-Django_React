from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models import CASCADE
from django.utils import timezone

from packages.models import Package
from user.manager import CustomUserManager


class Certification(models.Model):
    name = models.CharField(max_length=100)
    completion_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True, help_text='This is an email field')
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']


class Profile(models.Model):
    DateOfBirth = models.DateField(default=None, null=True, blank=True)
    hourly_rate = models.IntegerField()
    location = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    certifications = models.ManyToManyField(Certification)
    skills = models.ManyToManyField(Skill)
    package = models.OneToOneField(Package, on_delete=CASCADE)

    def __str__(self):
        return self.description


class Review(models.Model):
    comment = models.CharField(max_length=200, null=True)
    rating = models.IntegerField()

    EmployeeProfile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver of the review+')
    EmployerProfile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='provider of the review+')

    def __str__(self):
        return self.comment


class Account(models.Model):
    currency = models.CharField(max_length=20)
    type = models.CharField(max_length=15)
    balance = models.IntegerField()

    def __str__(self):
        return self.type
