from rest_framework.serializers import ModelSerializer 
from .models import File

class ImageSerializer(ModelSerializer):
    class Meta:
        model = File 
        fields = '__all__'
        # fields = ('id', 'name', 'image', 'created')

