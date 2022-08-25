from django.urls import path
from . import views

urlpatterns= [
    path('', views.challenge, name="challenge"),
]