from django.urls import path
from .views import PostApiView 

urlpatterns = [
    path('posts/' , PostApiView.as_view() , name="posts"),
    # path('user/' , UserApiView.as_view() , name="user")
]