from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

class NormalUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True)