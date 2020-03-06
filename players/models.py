from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    rank = models.CharField(max_length=5)
    age = models.IntegerField()
    elo = models.IntegerField()

