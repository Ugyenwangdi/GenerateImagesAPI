from rest_framework.serializers import ModelSerializer 
from .models import File, Image

class FileSerializer(ModelSerializer):
    class Meta:
        model = File 
        # fields = '__all__'
        fields = ('id', 'name', 'video', 'videolink')

class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image 
        # fields = '__all__'
        fields = ('id', 'name', 'height', 'width', 'imagelink')