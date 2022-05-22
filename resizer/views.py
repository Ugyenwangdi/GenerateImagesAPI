import os
from django.shortcuts import render
from django.conf import settings

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import File
from django.http import Http404, HttpResponse

from .serializers import ImageSerializer


# Create your views here.

def base(request):
    context = {
        'file': File.objects.all()
    }

    return render(request, 'base.html', context)

# def download(request, path):
#     file_path = os.path.join(settings.MEDIA_ROOT,path)

#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as fh:
#             response = HttpResponse(fh.read(), content_type = "application/adminupload")
#             response['Content-Disposition'] = 'inline;filename='+os.path.basename(file_path)
#             return response


#     return Http404


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
def getFiles(request):
    files = File.objects.all()

    serializer = ImageSerializer(files, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getFile(request, pk):
    file = File.objects.get(id=pk)

    serializer = ImageSerializer(file, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def generateImages(request):
    data = request.data 

    file = File.objects.create(
        name = data['name'],
        video = data['video']

    )

    serializer = ImageSerializer(file, many=False)

    return Response(serializer.data)


@api_view(['PUT'])
def updateFile(request, pk):
    data = request.data

    file = File.objects.get(id=pk)

    serializer = ImageSerializer(file, data=request.data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteFile(reqest, pk):
   file = File.objects.get(id=pk)
   file.delete()
   
   return Response('Image was deleted')