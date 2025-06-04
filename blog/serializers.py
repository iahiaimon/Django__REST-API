
from .models import User , Post



from rest_framework.serializers import ModelSerializer

class PostSerializers(ModelSerializer):
    class Meta:
        models = Post
        fields = '__all__'