from rest_framework.serializers import ModelSerializer

from .models import User , Post

class PostSerializers(ModelSerializer):
    class Meta:
        models = Post
        fields = '__all__'

class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
