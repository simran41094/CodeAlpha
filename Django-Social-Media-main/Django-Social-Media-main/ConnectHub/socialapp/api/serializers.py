from rest_framework.serializers import ModelSerializer
from socialapp.models import *

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        