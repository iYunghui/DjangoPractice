from django.urls import path
from . import views

urlpatterns = [
    path('upload/video', views.upload_video, name="upload_video"),
    path('upload/image', views.upload_image, name="upload_image"),
    path('video', views.video, name="video"),
    path('image', views.image, name="image"),
]