from django.urls import path
from content import views

urlpatterns = [
    path("units/" , views.units)
]
