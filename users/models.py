from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager



class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=False, null=False)
    image = models.ImageField(upload_to="users/profile/", null=True, blank=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = UserManager()