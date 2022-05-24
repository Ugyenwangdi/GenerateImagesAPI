from django.urls import path 
from django.urls import re_path 
from django.views.static import serve
from django.conf import settings


from . import views


urlpatterns = [
    path('', views.Home),

    ## for File
    path('routes', views.getRoutes),
    path('files', views.getFiles),
    path('files/upload', views.uploadFile),
    path('files/<str:pk>/update', views.updateFile),
    path('files/<str:pk>/delete', views.deleteFile),
    path('files/<str:pk>', views.getFile),

    ## for Image
    path('images', views.getImages),
    path('images/generate', views.generateImages),
    path('images/<str:pk>/update', views.updateImage),
    path('images/<str:pk>/delete', views.deleteImage),
    path('images/<str:pk>', views.getImage),

    path('download', views.Download),
    # re_path(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT})


]