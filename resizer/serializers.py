from rest_framework.serializers import ModelSerializer 
from .models import Image

class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image 
        fields = '__all__'
        # fields = ('id', 'name', 'image', 'created')

