from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from journal.models import Volume, Journal


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):  # user can have multiple roles at same time
    PUBLISHER = 1
    READER = 2
    ROLE_CHOICES = (
        (PUBLISHER, 'Publisher'),
        (READER, 'Reader'),
    )
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

    def __str__(self):
        return self.email


class Reader(CustomUser):
    liked_volumes = models.ManyToManyField(Volume)
    comments = models.CharField(max_length=300)


class Publisher(CustomUser):
    owned_journal = models.ManyToManyField(Journal)

