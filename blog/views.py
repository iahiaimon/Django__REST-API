from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post , User
from .serializers import PostSerializers, UserSerializers


# Create your views here.
class PostApiView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializers(posts, many=True).data

        return Response(serializer)

    def post(self , request):
        serializer = PostSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=201)

        return Response(serializer)
