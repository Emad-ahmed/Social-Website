from django.db import models
from django.contrib.auth.models import User


class Post_Info(models.Model):
    myuser = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
