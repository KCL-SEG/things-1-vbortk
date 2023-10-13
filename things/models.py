from django.db import models
from django.db.models import Model

class Thing(Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=120)
    quantity = models.IntegerField()
