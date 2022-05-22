from django.urls import path 

from . import views


urlpatterns = [

    path('', views.getRoutes),
    path('images/', views.getImages),
    path('images/resize/', views.resizeImage),
    path('images/<str:pk>/update/', views.updateImage),
    path('images/<str:pk>/delete/', views.deleteImage),
    path('images/<str:pk>/', views.getImage)
]