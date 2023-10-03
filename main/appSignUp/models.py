from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from djongo import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be staff')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser is set False')
        return self.create_user(email, password, **extra_fields)


class AutoIncrementCounter(models.Model):
    _id = models.CharField(primary_key=True, max_length=20)
    counter = models.IntegerField(default=1)


class CustomUser(AbstractBaseUser):
    user_id = models.CharField(primary_key=True, max_length=20, editable=False)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=100)

    name = models.CharField(max_length=100, default="-")
    nickname = models.CharField(max_length=150, default="-")
    telephone = models.CharField(max_length=100, default="-")
    address = models.CharField(max_length=100, default="-")
    gender = models.CharField(max_length=20, default="-")
    date_birth = models.CharField(max_length=20, default="-")

    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=20, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.user_id
