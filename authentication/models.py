from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if username is None:
            raise TypeError("Users must have a username.")
            
        user = self.model(username=username, email=self.normalize_email(email))

    def create_superuser(self, username, email, password, **extra_fields):
      """
      Create and return a `User` with superuser powers.

      Superuser powers means that this use is an admin that can do anything
      they want.
      """
      print('vao')
      if password is None:
          raise TypeError('Superusers must have a password.')

      user = self.create_user(username, email, password)
      user.is_superuser = True
      user.is_staff = True
      user.save()

      return user


class User(AbstractBaseUser):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email