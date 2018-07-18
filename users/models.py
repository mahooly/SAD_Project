from django.contrib.auth.models import AbstractUser
from django.db import models
from .choices import *


class CustomUser(AbstractUser):
    state = models.NullBooleanField(default=None)
    isBen = models.BooleanField(default=False)
    isOrg = models.BooleanField(default=False)
    image = models.ImageField(upload_to='profile_pics/', default='/profile_pics/no-picture.png')

    def __str__(self):
        return self.username


class Benefactor(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='benefactor')
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=10, choices=SEX_CHOICES, default='Male')
    day = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    education = models.CharField(max_length=10, choices=EDUCATION_CHOICES, default='nothing')
    major = models.CharField(max_length=20, blank=True)
    nationalId = models.CharField(max_length=10)
    city = models.CharField(max_length=10, choices=CITY_CHOICES, default='blank')
    address = models.CharField(max_length=100, default='st')
    phone = models.CharField(max_length=12)


class Organizer(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='organizer')
    name = models.CharField(max_length=20)
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=10, choices=CITY_CHOICES, default='blank')
    phone = models.CharField(max_length=15)
    website = models.URLField()
    license = models.CharField(max_length=20)


class Project(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='creator')
    name = models.CharField(max_length=50)
    budget = models.CharField(max_length=10)
    city = models.CharField(max_length=15, choices=CITY_CHOICES)
    description = models.TextField(max_length=300)
    paymethod = models.CharField(max_length=10, choices=BANK_CHOICES)
    cardno = models.CharField(max_length=20, blank=True)
    accno = models.CharField(max_length=25, blank=True)
    alreadyPaid = models.IntegerField(default=0)


class Rate(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='rater')
    ratedUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='rated')
    f1 = models.IntegerField()
    f2 = models.IntegerField()
    f3 = models.IntegerField()
    f4 = models.IntegerField()
    f5 = models.IntegerField()
    description = models.TextField(max_length=300)


class Ability(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)


class UserAbilities(models.Model):
    class Meta:
        unique_together = ('abilityId', 'username')

    abilityId = models.ForeignKey(Ability, on_delete=models.CASCADE, related_name='ability')
    username = models.ForeignKey(CustomUser, to_field='username', on_delete=models.CASCADE, related_name='benefactorusername')


class WeeklySchedule(models.Model):
    id = models.AutoField(primary_key=True)



# class Requirement(models.Model):
#     class Meta:
#         unique_together = ('id', 'wId')
#
#     id = models.AutoField()
#     city = models.CharField(max_length=20)
#     address = models.CharField(max_length=100)
#     gender = models.CharField(max_length=10)
#     wId = models.ForeignKey(WeeklySchedule, on_delete=models.CASCADE, related_name='week')


# class RequirementAbilities(models.Model):
#     class Meta:
#         unique_together = ('abilityId', 'reqId')
#
#     reqId = models.ForeignKey(Requirement, on_delete=models.CASCADE, related_name='req')
#     abilityId = models.ForeignKey(Ability, on_delete=models.CASCADE, related_name='ab')


class Report(models.Model):
    id = models.AutoField(primary_key=True)
    benefactor = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='ben')
    organization = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='org')
    type = models.CharField(max_length=1)
    description = models.TextField(max_length=100, blank=True)
    operator = models.CharField(max_length=1)
    rateId = models.ForeignKey(Rate, on_delete=models.DO_NOTHING, related_name='rate')
    wId = models.ForeignKey(WeeklySchedule, on_delete=models.DO_NOTHING, related_name='weekly')
    payment = models.CharField(max_length=10)

