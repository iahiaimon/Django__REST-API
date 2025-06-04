from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from rest_framework.views import APIView

from .models import Post , User
from .serializers import PostSerializer, UserSerializer


# Create your views here.
class PostsApiView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True).data
