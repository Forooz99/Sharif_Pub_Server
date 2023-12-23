from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email or len(email) <= 0:
            raise ValueError("Email required")
        if not password:
            raise ValueError("Password required")

        user = self.model(email=self.normalize_email(email), )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser):
    class Types(models.TextChoices):  # 2 different types of user
        READER = "READER", "reader"
        PUBLISHER = "PUBLISHER", "publisher"

    username = models.CharField(max_length=50)
    student_number = models.CharField(max_length=8, validators=[RegexValidator(regex='^[0-9]{8}$', message='student-number must have 8 digits')])
    email = models.EmailField(max_length=200, unique=True)
    type = models.CharField(max_length=8, choices=Types.choices, default=Types.READER)  # default user is reader
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # if new user is publisher or reader
    is_reader = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    # defining the manager for the UserAccount model
    objects = UserAccountManager()

    def __str__(self):
        return str(self.email)

    def save(self, *args, **kwargs):
        if not self.type or self.type == None:
            self.type = UserAccount.Types.PUBLISHER
        return super().save(*args, **kwargs)


class ReaderManager(models.Manager):

    def create_user(self, email, password=None):
        if not email or len(email) <= 0:
            raise ValueError("Email required")
        if not password:
            raise ValueError("Password required")
        email = email.lower()
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(type=UserAccount.Types.READER)
        return queryset


class Reader(UserAccount):
    class Meta:
        proxy = True

    objects = ReaderManager()

    def save(self, *args, **kwargs):
        self.type = UserAccount.Types.READER
        self.is_reader = True
        return super().save(*args, **kwargs)


class PublisherManager(models.Manager):

    def create_user(self, email, password=None):
        if not email or len(email) <= 0:
            raise ValueError("Email required")
        if not password:
            raise ValueError("Password required")
        email = email.lower()
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(type=UserAccount.Types.PUBLISHER)
        return queryset


class Publisher(UserAccount):
    class Meta:
        proxy = True

    objects = PublisherManager()

    def save(self, *args, **kwargs):
        self.type = UserAccount.Types.PUBLISHER
        self.is_publisher = True
        return super().save(*args, **kwargs)
