from rest_framework.decorators import api_view
from rest_framework.response import Response
from socialapp.models import *
from .serializers import *

@api_view(['GET', 'POST']) # This decorator allows us to use function based views instead of class based views
def getRoutes(request):
    routes = [
        'GET /api',
        # 'GET /api/users',
        # 'GET /api/users/id',
        # 'POST /api/login',
        # 'GET /api/users/profile',
        'GET /api/posts',
        'GET /api/posts/id',
    ]

    return Response(routes)

@api_view(['GET'])
def getPosts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True) # many = True means we are serializing multiple objects
    return Response(serializer.data)

@api_view(['GET'])
def getPost(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getProfile(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

# @api_view(['POST'])
# def createPost(request):
#     data = request.data
#     user = request.user
#     post = Post.objects.create(
#         user=user,
#         body=data['body'],
#     )
#     serializer = PostSerializer(post, many=False)
#     return Response(serializer.data)
