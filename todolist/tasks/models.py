from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # login = models.CharField(max_length=50, unique=True) # Unique so there are no duplicates
    # pswd = models.CharField(max_length=50)
    pass

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE) # So when user is deleted, all his tasks are also deleted