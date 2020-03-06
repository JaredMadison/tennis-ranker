from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    rank = models.CharField(max_length=5)
    age = models.IntegerField(default=30)
    elo = models.IntegerField(default=1500)

