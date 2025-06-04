from django.shortcuts import render , redirect
from django.http import HttpResponse , JsonResponse

# Create your views here.
def post(request):
    return HttpResponse("this is post")
    