from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name,username,email, password=None):
        if not email:
            raise ValueError('el usuario debe ingresar un email')

        if not username:
            raise ValueError('el usuario debe ingresar un username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,

        )
        user.save(using=self._db)
        return user



# Create your models here.
class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    username = models.CharField(max_length=150, unique=True)
    phone_number = models.CharField(max_length=150)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    objects = MyAccountManager()

    def __str__(self):
        return self.email