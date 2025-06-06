from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.


class CustomUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    # def set_password(self, raw_password):
    #     """Hash and set the user's password."""
    #     self.password = make_password(raw_password)

    # def check_password(self, raw_password):
    #     """Verify the user's password."""
    #     return check_password(raw_password, self.password)

    # class Meta:
    #     verbose_name = "User"
    #     verbose_name_plural = "Users"


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
