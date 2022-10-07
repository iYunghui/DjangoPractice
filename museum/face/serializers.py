from rest_framework import serializers
from .models import Media
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

class ImageSerializer(serializers.Serializer):
    def validate_file_size(value):
        filesize = value.size
        if filesize > 20971520: # 20 MB
            raise ValidationError("Too large")
        return value

    upload_file = serializers.ImageField(validators=[FileExtensionValidator(['jpg', 'png']), validate_file_size])

class VideoSerializer(serializers.Serializer):
    def validate_file_size(value):
        filesize = value.size
        if filesize > 20971520: # 20 MB
            raise ValidationError("Too large")
        if filesize < 1572864:  # 1.5 MB
            raise ValidationError("Too small")
        return value

    upload_file = serializers.FileField(validators=[FileExtensionValidator(['mp4', 'mkv']), validate_file_size])