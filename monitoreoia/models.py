from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    # Your custom fields go here
    objects = CustomUserManager()




