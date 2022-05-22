from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Image

from .serializers import ImageSerializer


# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [

        {
            'Endpoint': '/image/',
            'method': 'Get',
            'image': {'image': ""},
            'description': 'Return cropped image from the database'
        },
        {
            'Endpoint': '/image/resize',
            'method': 'Get',
            'image': {'image': ""},
            'description': 'Resize the image sent in Post request'
        }
    ]

    return Response(routes)

@api_view(['GET'])
def getImages(request):
    image = Image.objects.all()

    serializer = ImageSerializer(image, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getImage(request, pk):
    image = Image.objects.get(id=pk)

    serializer = ImageSerializer(image, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def resizeImage(request):
    data = request.data 

    image = Image.objects.create(
        name = data['name'],
        image = data['image']

    )

    serializer = ImageSerializer(image, many=False)

    return Response(serializer.data)


@api_view(['PUT'])
def updateImage(request, pk):
    data = request.data

    image = Image.objects.get(id=pk)

    serializer = ImageSerializer(image, data=request.data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteImage(reqest, pk):
   image = Image.objects.get(id=pk)
   image.delete()
   
   return Response('Image was deleted')