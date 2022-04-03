from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.utils.timezone import now

#  Crate Custom User Model
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a User with the given email and password
        """
        if not email:
            raise ValueError('User must have an email address.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a Superuser with the given email and Password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_seller', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone number format '+919999999999' ")
    phone = models.CharField('Phone', validators=[phone_regex], max_length=10, unique=False, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    data_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    full_name = models.CharField(default="", max_length=255, blank=True)
    REQUIRED_FIELD = ['username', 'full_name']

    object = UserManager()


class UserOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now=True)
    otp = models.SmallIntegerField()

