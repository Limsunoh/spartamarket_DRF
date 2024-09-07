from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    first_name = None
    last_name = None
    email = models.EmailField(unique=True, blank=False)
    nickname = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    birth_date = models.DateField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
