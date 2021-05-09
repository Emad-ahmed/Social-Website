from django.db import models
from django.contrib.auth.models import User


class Profile_Post(models.Model):
    myid = models.IntegerField(unique=True)
    image = models.ImageField(upload_to='profile/')
