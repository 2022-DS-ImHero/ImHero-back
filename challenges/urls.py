from django.urls import path
from . import views

urlpatterns= [
    path('', views.challenge, name='challenge'),
    path('category/<str:slug>', views.category_page),
    
]