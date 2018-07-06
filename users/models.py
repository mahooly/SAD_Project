from django.contrib.auth.models import AbstractUser
from django.db import models
from .choices import *


class CustomUser(AbstractUser):
    state = models.NullBooleanField(default=None)
    isBen = models.BooleanField(default=False)
    isOrg = models.BooleanField(default=False)
    image = models.ImageField(upload_to='profile_pics/', default='profile_pics/no-picture.png')

    def __str__(self):
        return self.username


class Benefactor(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='benefactor')
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=10, choices=SEX_CHOICES, default='Male')


class Organizer(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='organizer')
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    website = models.URLField()
    license = models.CharField(max_length=20)


class Project(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=50)
    budget = models.CharField(max_length=1, choices=BANK_CHOICES)
    city = models.CharField(max_length=15, choices=CITY_CHOICES)
    description = models.TextField(max_length=300)
    paymethod = models.CharField(max_length=2, choices=BANK_CHOICES)
    cardno = models.CharField(max_length=20, blank=True)
    accno = models.CharField(max_length=25, blank=True)
    alreadyPaid = models.IntegerField()
