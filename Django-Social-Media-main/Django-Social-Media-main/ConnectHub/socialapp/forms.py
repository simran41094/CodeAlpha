from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm

class MyUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class CustomUserProfile(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'bio', 'profile_pic']

class CustomUserBio(ModelForm):
    class Meta:
        model = User
        fields = ['gender', 'address', 'email', 'phone_number']

class CreatePost(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['owner']