import os
import cv2
from django.shortcuts import render
from django.conf import settings

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import File, Image
from django.http import Http404, HttpResponse

from .serializers import FileSerializer, ImageSerializer


# Create your views here.


def Home(request):
    return render(request, 'home.html')

def Download(request):
    context = {
        'images': Image.objects.all()
    }

    return render(request, 'download.html', context)

# def download(request, path):
#     file_path = os.path.join(settings.MEDIA_ROOT,path)

#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as fh
#             response = HttpResponse(fh.read(), content_type = "application/video")
#             response['Content-Disposition'] = 'inline;filename='+os.path.basename(file_path)
#             return response


#     return Http404

# get all the routes

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/routes',
            'method': 'Get',
            'image': {'image': ""},
            'description': 'Return files uploaded to the database'
        },
        {
            'Endpoint': '/files',
            'method': 'Get',
            'image': {'image': ""},
            'description': 'Return files from the database'
        },
        {
            'Endpoint': '/files/pk',
            'method': 'Get',
            'image': {'image': ""},
            'description': 'Return single file using pk from the database'
        },
        {
            'Endpoint': '/files/upload',
            'method': 'Post',
            'image': {'image': ""},
            'description': 'Upload a file'
        },
        {
            'Endpoint': '/files/pk/update',
            'method': 'Put',
            'image': {'image': ""},
            'description': 'Update the file using pk'
        },
        {
            'Endpoint': '/files/pk/delete',
            'method': 'Delete',
            'image': {'image': ""},
            'description': 'Delete the file using pk'
        },
        {
            'Endpoint': '/images',
            'method': 'Get',
            'image': {'image': ""},
            'description': 'Get generated images'
        },
        {
            'Endpoint': '/images/<str:pk>',
            'method': 'Delete',
            'image': {'image': ""},
            'description': 'Get image using pk'
        },
        {
            'Endpoint': '/images/generate',
            'method': 'Post',
            'image': {'image': ""},
            'description': 'Upload images generated from video file '
        },
        {
            'Endpoint': '/images/<str:pk>/update',
            'method': 'Put',
            'image': {'image': ""},
            'description': 'Update an image'
        },
        {
            'Endpoint': '/images/<str:pk>/delete',
            'method': 'Delete',
            'image': {'image': ""},
            'description': 'Delete the image using pk'
        },
        {
            'Endpoint': '/download',
            'description': 'Show the download page'
        }
    ]

    return Response(routes)

######## Endpoints for Files ###########
@api_view(['GET'])
def getFiles(request):
    files = File.objects.all()

    serializer = FileSerializer(files, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getFile(request, pk):
    file = File.objects.get(id=pk)

    serializer = FileSerializer(file, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def uploadFile(request):

    videos = File.objects.all()
    videos.delete()
    images = Image.objects.all()
    images.delete()

    data = request.data 

    video = data['video']

    file = File.objects.create(
        name = data['name'],
        video = video,
        videolink = 'http://127.0.0.1:8000/media/videos/'+str(video)

    )

    # files = File.objects.all()
    # # print(videos)
    # for vd in files:
    #     videolink = vd.videolink
    #     break

    # print(videolink)


    # video = cv2.VideoCapture(videolink)


    # # frame
    # currentframe = 0
    # while(video.isOpened()):
        
    #     # reading from frame
    #     ret, frame = video.read()

    #     if ret:
    #         # if video is still left continue creating images
    #         name = str(currentframe) + '.jpg'
    #         print ('Creating...' + name)

    #         # let's downscale the image using new  width and height
    #         # width = 300
    #         # height = 300
    #         dimension = (width, height)
    #         frame = cv2.resize(frame, dimension, interpolation= cv2.INTER_LINEAR)

    #         # # let's upscale the image using new  width and height
    #         # up_width = 1200
    #         # up_height = 900
    #         # up_points = (up_width, up_height)
    #         # frame = cv2.resize(frame, up_points, interpolation= cv2.INTER_LINEAR)
            
    #         # writing the extracted images

    #         if currentframe%1 == 0:
    #             #http://127.0.0.1:8000/media/0.jpg
    #             cv2.imwrite(os.path.join(settings.MEDIA_ROOT, name), frame)  

    #             # I want to save inside Image model
    #             image = Image.objects.create(
    #                 name = name,
    #                 height = height, 
    #                 width = width,
    #                 image = name,
    #                 imagelink = 'http://127.0.0.1:8000/media/'+ name

    #             )

    
    #         # increasing counter 
    #         # to name images with number of images created
    #         currentframe += 1

    #         if currentframe == 5:
    #             break
    #     else:
    #         break

    # # Release all space and windows once done
    # video.release()
    # cv2.destroyAllWindows()

    # images = Image.objects.all()
    # serializer = ImageSerializer(images, many=True)

    serializer = FileSerializer(file, many=False)
    

    return Response(serializer.data)


@api_view(['PUT'])
def updateFile(request, pk):
    data = request.data

    file = File.objects.get(id=pk)

    serializer = FileSerializer(file, data=request.data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteFile(reqest, pk):
   file = File.objects.get(id=pk)
   file.delete()
   
   return Response('Image was deleted')



############ Endpoints For images ##########

@api_view(['GET'])
def getImages(request):
    images = Image.objects.all()

    serializer = ImageSerializer(images, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getImage(request, pk):
    image = Image.objects.get(id=pk)

    serializer = ImageSerializer(image, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def generateImages(request):

    # empty database before using the videos and images
    videos = File.objects.all()
    videos.delete()
    images = Image.objects.all()
    images.delete()


    data = request.data 

    video = data['video']
    height = int(data['height'])
    width = int(data['width'])

    file = File.objects.create(
        name = data['name'],
        video = video,
        videolink = 'http://127.0.0.1:8000/media/videos/'+str(video)

    )

    files = File.objects.all()
    # take only one video file
    for vd in files:
        videolink = vd.videolink
        print(videolink)

        break



    video = cv2.VideoCapture(videolink)


    # frame
    currentframe = 0
    while(video.isOpened()):
        
        # reading from frame
        ret, frame = video.read()

        if ret:
            # if video is still left continue creating images
            name = str(currentframe) + '.jpg'
            print ('Creating...' + name)

            # let's downscale the image using new  width and height
            # width = 300
            # height = 300
            dimension = (width, height)
            frame = cv2.resize(frame, dimension, interpolation= cv2.INTER_LINEAR)

            # # let's upscale the image using new  width and height
            # up_width = 1200
            # up_height = 900
            # up_points = (up_width, up_height)
            # frame = cv2.resize(frame, up_points, interpolation= cv2.INTER_LINEAR)
            
            # writing the extracted images

            if currentframe%10 == 0:
                #http://127.0.0.1:8000/media/0.jpg
                cv2.imwrite(os.path.join(settings.MEDIA_ROOT, name), frame)  

                # I want to save inside Image model
                image = Image.objects.create(
                    name = name,
                    height = height, 
                    width = width,
                    image = name,
                    imagelink = 'http://127.0.0.1:8000/media/'+ name

                )

    
            # increasing counter 
            # to name images with number of images created
            currentframe += 1

            if currentframe == 5:
                break
        else:
            break

    # Release all space and windows once done
    video.release()
    cv2.destroyAllWindows()

    images = Image.objects.all()
    serializer = ImageSerializer(images, many=True)

    return Response(serializer.data)


@api_view(['PUT'])
def updateImage(request, pk):
    data = request.data

    image = Image.objects.get(id=pk)

    serializer = ImageSerializer(image, data=data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteImage(request, pk):
   image = Image.objects.get(id=pk)
   image.delete()
   
   return Response('Image was deleted')