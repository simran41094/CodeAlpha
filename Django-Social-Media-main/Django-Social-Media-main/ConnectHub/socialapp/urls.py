from django.urls import path
from . import  views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginUser, name='login'),
    path('register/', views.signupUser, name='signup'),
    path('logout/', views.logoutUser, name='logout'),
    path('create-post/', views.createPost, name='create-Post'),
    path('update-post/<str:pk>/', views.updatePost, name='update-Post'),
    path('delete-post/<str:pk>/', views.deletePost, name='delete-Post'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('edit-Profile/<str:pk>/', views.editProfile, name='edit-Profile'),
    path('edit-Bio/<str:pk>/', views.editBio, name='edit-Bio'),
    path('post/<str:pk>/', views.post, name='post'),
    path('notifications/', views.notifications, name='notifications'),
    
]