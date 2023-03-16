from django.db import models
from django.contrib.auth.models import AbstractUser
from content.models import TechStack


class User(AbstractUser):
    google_id = models.CharField(max_length=100, blank=True, null=True)
    tech_stack = models.ManyToManyField(TechStack, blank=True)
    is_premium = models.BooleanField(("Premium"), default=False)