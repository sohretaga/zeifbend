from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField()
    balacne = models.FloatField(default=0)
    level = models.IntegerField(default=0)
    leaderboard = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='avatars')
    total_game_count = models.IntegerField(default=0)
    won_game_count = models.IntegerField(default=0)
