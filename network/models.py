from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

# Posts class
class Post(models.Model):
    content = models.TextField()
    dateTime = models.DateTimeField(auto_now = False, auto_now_add = True)
    like = models.BigIntegerField(default = 0)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "user")

    def __str__(self):
        return f"{self.user} | {self.content}"

class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    followingUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")

    def __str__(self):
        return f"{self.user} is following {self.followingUser}"