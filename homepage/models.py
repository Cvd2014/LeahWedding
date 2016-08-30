from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Bride(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='WeddingParty')

    def __str__(self):
        return self.name


class Groom(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='WeddingParty')

    def __str__(self):
        return self.name


class Party(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='WeddingParty')
    role = models.CharField(max_length=200)
    brideside = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Venue(models.Model):
    church=models.BooleanField(default=True)
    name=models.CharField(max_length=500)
    url=models.URLField()



