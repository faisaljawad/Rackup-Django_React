from django.db import models
from django.db.models import CASCADE
from user.models import Profile, Skill


class Project(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=700)
    employer = models.OneToOneField(Profile, on_delete=CASCADE, related_name='Employeer')
    skills_required = models.ForeignKey(Skill, on_delete=CASCADE)

    employee = models.ManyToManyField(Profile, related_name='FreeLancer')

    def __str__(self):
        return self.name


class Proposal(models.Model):
    cover_letter = models.CharField(max_length=500)
    price_quotation = models.IntegerField()
    deadline = models.DateField()
    submitted_by = models.ForeignKey(Profile, on_delete=CASCADE)
    skills = models.ForeignKey(Skill, on_delete=CASCADE)

    def __str__(self):
        return self.cover_letter
