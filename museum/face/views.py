from django.shortcuts import render, get_object_or_404, redirect
from .forms import UploadImageForm, UploadVideoForm
from .models import Media
from django.urls import reverse
import datetime
import os
from pony.orm import *
import json
from django.http import HttpResponse, JsonResponse, FileResponse
from django.core import serializers
import mimetypes


# Create your views here.
def upload(request):
    if request.method == 'GET':
        image_form = UploadImageForm()
        video_form = UploadVideoForm()
    
    return render(request, 'face/upload.html', {'image_form': image_form, 'video_form': video_form})

def upload_video(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass
    

def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            write_to_DB(request.FILES['upload_file'].name, "image")            
            handle_uploaded_file(request.FILES['upload_file'], "image")
            return HttpResponse("upload success", status=200)
        else:
            return HttpResponse(form.errors.as_json())
    elif request.method == 'GET':
        image_files = search_in_DB("", "image")
        # image_files = serializers.serialize('json', image_files)
        print(image_files)
        return JsonResponse(image_files, safe=False)
    else:
        return redirect("/api/face/upload")

def video(request, filename):
    if request.method == 'GET':
        pass

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
        Media(uid=os.path.splitext(filename)[0], type=filetype, media_filename=filename, upload_timestamp=datetime.datetime.now())

def search_in_DB(filename, filetype):
    with db_session:
        if filename == "":
            files = select(f for f in Media if f.type == filetype)
            lists = []
            for f in files:
                lists.append({"id": f.id, "uid": f.uid, "type": filetype, "media_filename": f.media_filename})
            return lists