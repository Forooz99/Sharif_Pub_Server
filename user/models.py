from django.db import models
from django.contrib.auth.models import AbstractUser
from journal.models import Volume, Journal


class User(AbstractUser):  # user can have multiple roles at same time
    # is_admin = models.BooleanField('Is admin', default=False)
    is_reader = models.BooleanField('Is reader', default=False)
    is_publisher = models.BooleanField('Is publisher', default=False)


class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    liked_volumes = models.ManyToManyField(Volume)
    comments = models.CharField(max_length=300)


class Publisher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    owned_journal = models.ManyToManyField(Journal)

