from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from timezone_field import TimeZoneField
import string
import random

# Create your models here.
def random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for m in range(length))

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not username:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        # print(email)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class User(AbstractUser):
    id = models.SlugField(max_length=255, unique=True, primary_key=True)
    real_name = models.CharField(max_length=50)
    tz = TimeZoneField(default="Asia/Kolkata")

    class Meta:
        ordering = ('id',)
    
    def save(self, *args, **kwargs):
        if not self.id:
            random_str = random_string(9)
            self.id = random_str
            super().save(*args, **kwargs)


class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="activity_periods")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return "{} - {} to {}".format(self.user, self.start_time, self.end_time)