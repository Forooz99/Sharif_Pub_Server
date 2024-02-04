from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from journal.models import Volume, Journal
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Types(models.TextChoices):
        READER = "READER", "reader"
        PUBLISHER = "PUBLISHER", "publisher"

    type = models.CharField(max_length=10, choices=Types.choices, default=Types.READER)
    email = models.EmailField(primary_key=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Reader(CustomUser):
    liked_volumes = models.ManyToManyField(Volume, blank=True)
    comments = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        permissions = [
            ('can_read', 'Can read volumes'),
            ('can_like', 'Can like volumes'),
        ]
        db_table = 'Reader'


class Publisher(CustomUser):
    owned_journal = models.ManyToManyField(Journal)

    class Meta:
        permissions = [
            ('can_read', 'Can read volumes'),
            ('can_publish', 'Can publish volumes'),
            ('can_delete', 'Can delete volumes'),
            ('can_edit', 'Can edit volumes'),
        ]
        db_table = 'Publisher'
