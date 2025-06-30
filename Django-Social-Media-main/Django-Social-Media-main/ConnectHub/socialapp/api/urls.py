from . import views
from django.urls import path

urlpatterns = [
    path('', views.getRoutes),
    path('posts/', views.getPosts),
    path('posts/<str:pk>/', views.getPost),
    path('profile/<str:pk>/', views.getProfile),
    # path('create-post/', views.createPost),
]