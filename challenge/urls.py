from django.urls import path
from . import views

urlpatterns= [
    path('', views.challenge, name="challenge"),
    path('professor/detail/<int:post_id>/', views.p_detail, name="p_detail"),
    path('create_comment/<int:post_id>', views.create_comment, name='create_comment'),

    path('company/detail/<int:post_id>/', views.c_detail, name="c_detail"),
    path('senior/detail/<int:post_id>/', views.s_detail, name="s_detail"),

    path('professor/detail/<int:post_id>/likes/', views.likes, name='likes'),
]