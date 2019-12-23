from django.db import models
from django.db.models import CASCADE

from packages.models import Package


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


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    dob = models.DateTimeField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.name


class Review(models.Model):
    comment = models.CharField(max_length=200, null=True)
    rating = models.IntegerField()

    def __str__(self):
        return self.comment


class Profile(models.Model):
    age = models.IntegerField()
    hourly_rate = models.IntegerField()
    location = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    user = models.OneToOneField(User, on_delete=CASCADE)
    certifications = models.ForeignKey(Certification, on_delete=CASCADE)
    skills = models.ForeignKey(Skill, on_delete=CASCADE)
    reviews = models.ForeignKey(Review, on_delete=CASCADE)
    package = models.OneToOneField(Package, on_delete=CASCADE)

    def __str__(self):
        return self.description


class Account(models.Model):
    currency = models.CharField(max_length=20)
    type = models.CharField(max_length=15)
    balance = models.IntegerField()

    def __str__(self):
        return self.type
