from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


# Posts class
class Post(models.Model):
    content = models.TextField()
    dateTime = models.DateTimeField(auto_now = False, auto_now_add = True)
    like = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "user")