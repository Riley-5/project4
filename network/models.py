from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    following = models.BigIntegerField(null = True)
    checkFollowing = models.BooleanField(null = True)


# Posts class
class Post(models.Model):
    content = models.TextField()
    dateTime = models.DateTimeField(auto_now = False, auto_now_add = True)
    like = models.BigIntegerField(default = 0)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "user")

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user.username,
            "content": self.content,
            "timestamp": self.dateTime.strftime("%b %d %Y, %I:%M %p"),
            "like": self.like
        }
