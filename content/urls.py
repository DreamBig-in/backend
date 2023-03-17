from django.urls import path
from content import views

urlpatterns = [
    path("units/" , views.units),
    path("chat/" , views.ChatGPT, name="chat"),
]
