from django.shortcuts import render, get_object_or_404, redirect
from .forms import UploadImageForm, UploadVideoForm
from .models import Media
from .serializers import ImageSerializer, VideoSerializer
from django.urls import reverse
import datetime
import os
from pony.orm import *
import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, FileResponse
from rest_framework.generics import GenericAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

# Create your views here.
class Upload(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'face/upload.html'
    serializer_class = ImageSerializer

    def get(self, request):
        image_form = ImageSerializer
        video_form = VideoSerializer
        
        return Response({'image_form': image_form, 'video_form': video_form})


class UploadVideo(APIView):
    def get(self, request):
        video_files = search_in_DB("", "video")
        return JsonResponse(video_files, safe=False)

    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        if not serializer.is_valid():
            return HttpResponse(serializer.error_messages)
        write_to_DB(request.FILES['upload_file'].name, "video")            
        handle_uploaded_file(request.FILES['upload_file'], "video")
        return HttpResponse("upload success", status=200)

class UploadImage(APIView):
    def get(self, request):
        image_files = search_in_DB("", "image")
        return JsonResponse(image_files, safe=False)

    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if not serializer.is_valid():
            return HttpResponse(serializer.error_messages)
        write_to_DB(request.FILES['upload_file'].name, "image")            
        handle_uploaded_file(request.FILES['upload_file'], "image")
        return HttpResponse("upload success", status=200)


def video(request, filename):
    if request.method == 'GET':
        
        return FileResponse(open('face/static/'+"video"+'/'+str(filename), 'rb'), as_attachment=True)

def image(request, filename):
    if request.method == 'GET':
        return FileResponse(open('face/static/'+"image"+'/'+str(filename), 'rb'), as_attachment=True)

def handle_uploaded_file(f, type):
    print('handle_uploaded_file')
    with open('face/static/'+type+'/'+f.name, 'wb+') as destination:  
        print('face/static/'+type+'/'+f.name)
        for chunk in f.chunks():  
            destination.write(chunk)
    print("finish")

def write_to_DB(filename, filetype):
    with db_session:
        files = select(f for f in Media if f.type == filetype)
        has_record = 0
        for f in files:
            if f.media_filename == filename:
                f.upload_timestamp = datetime.datetime.now()
                has_record = 1
                break
        if has_record == 0:
            Media(uid=os.path.splitext(filename)[0], type=filetype, media_filename=filename, upload_timestamp=datetime.datetime.now())

def search_in_DB(filename, filetype):
    with db_session:
        if filename == "":
            files = select(f for f in Media if f.type == filetype)
            lists = []
            for f in files:
                lists.append({"id": f.id, "uid": f.uid, "type": filetype, "media_filename": f.media_filename})
            return lists