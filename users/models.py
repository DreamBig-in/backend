from django.db import models
from django.contrib.auth.models import AbstractUser
from content.models import TechStack


class User(AbstractUser):
    tech_stack = models.ManyToManyField(TechStack, blank=True)
    
    is_premium = models.BooleanField(("Premium"), default=False)