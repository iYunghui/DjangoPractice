from django import forms
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError


class UploadImageForm(forms.Form):

    def validate_file_size(value):
        filesize = value.size
        if filesize > 20971520: # 20 MB
            raise ValidationError("Too large")
        return value
    
    upload_file = forms.ImageField(label="select a file", help_text="", validators=[FileExtensionValidator(['jpg', 'png']), validate_file_size])

class UploadVideoForm(forms.Form):

    def validate_file_size(value):
        filesize = value.size
        if filesize > 20971520: # 20 MB
            raise ValidationError("Too large")
        if filesize < 1572864:  # 1.5 MB
            raise ValidationError("Too small")
        return value

    upload_file = forms.FileField(label="select a file", help_text="", validators=[FileExtensionValidator(['mp4', 'mkv']), validate_file_size])