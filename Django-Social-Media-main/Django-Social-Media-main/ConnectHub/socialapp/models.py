from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, unique=True, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    gender = models.ForeignKey('Gender',null=True ,on_delete=models.CASCADE)
    phone_number = models.IntegerField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, default="avatar.svg") 

    def __str__(self):
        return self.username


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.TextField(null=True, blank=True)
    tag = models.ForeignKey('Tag', null=True, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, default="default.jpg")

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return f"Post by {self.owner.username}"


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like by {self.owner.username} on {self.post}"


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Gender(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    