from django.urls import path 
from django.urls import re_path as url
from django.views.static import serve
from django.conf import settings


from . import views


urlpatterns = [

    path('', views.getRoutes),
    path('files/', views.getFiles),
    path('files/generateimg/', views.generateImages),
    path('files/<str:pk>/update/', views.updateFile),
    path('files/<str:pk>/delete/', views.deleteFile),
    path('files/<str:pk>/', views.getFile),


    path('download/', views.base),
    # url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),

]