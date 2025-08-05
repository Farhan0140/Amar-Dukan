from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager


class User( AbstractUser ):
    username = None
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True)

    profile_image = models.ImageField(upload_to="profile_images/", blank=True, null=True, default="profile_images/default.jpg")

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'    # username er poriborte kon field ta use korte chai, eakhon theke username er poriborte email diea login korte parbo
    REQUIRED_FIELDS = []    # superuser create korar jonno username tai required field hisebe thake