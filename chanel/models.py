from django.db import models
from account.models import CustomUser

# Create your models here.

class Chanel(models.Model):
    name = models.CharField(max_length=1000)
    user_count = models.IntegerField()
    users = models.ManyToManyField(CustomUser)
    deposit = models.FloatField()
    tour_count = models.IntegerField()
    