from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tweet = models.CharField(max_length=150)

    def __str__(self):
        return f"tweet user: {self.username} tweet: {self.tweet}"
    

    