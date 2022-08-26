from django.urls import path
from . import views

urlpatterns= [
    path('', views.challenge, name='challenge'),
    path('detail/<int:post_id>/', views.detail, name='detail'),
    path('category/<str:slug>', views.category_page),
    path('create_comment/<int:post_id>', views.create_comment, name='create_comment'),
    
    
]