from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('upload/', views.upload, name="upload"),
    path('upload/', views.Upload.as_view(), name="upload"),
    path('upload/video/', views.UploadVideo.as_view(), name="upload_video"),
    path('upload/image/', views.UploadImage.as_view(), name="upload_image"),
    path('video/<str:filename>', views.video, name="video"),
    path('image/<str:filename>', views.image, name="image")
]