from django.contrib import admin
from content import models

# Register your models here.
admin.site.register(models.TechStack)
admin.site.register(models.Content)
admin.site.register(models.Tags)
admin.site.register(models.Questions)