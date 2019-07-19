from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserAccount(AbstractUser):
    ulica = models.CharField(max_length=100)
    numer_domu = models.CharField(max_length=5)
    kod_pocztowy = models.CharField(max_length=10)
    miasto = models.CharField(max_length=100)
    telefon = models.CharField(max_length=9)
    