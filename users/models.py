from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import BigAutoField

class User(AbstractUser):
    bio = models.TextField(blank=True)