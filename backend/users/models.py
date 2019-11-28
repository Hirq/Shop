from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserAccount(AbstractUser):
    full_name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    number_house = models.CharField(max_length=5)
    post_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=9)
    