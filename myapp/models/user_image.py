from django.db import models
from django.contrib.auth.models import User


class Image_Post(models.Model):
    myuser = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=122)
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField(auto_now_add=True)
