from django.db import models

class UserInfo(models.Model):
    """A class that define user database"""
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
