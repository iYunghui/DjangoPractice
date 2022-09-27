from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload, name="upload"),
    path('upload/video/', views.upload_video, name="upload_video"),
    path('upload/image/', views.upload_image, name="upload_image"),
    path('video/<str:filename>', views.video, name="video"),
    path('image/<str:filename>', views.image, name="image"),
]