from django.db import models


class Package(models.Model):
    name = models.CharField(max_length=20)
    bids_count = models.IntegerField()
    validity = models.IntegerField()
    price = models.IntegerField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name
