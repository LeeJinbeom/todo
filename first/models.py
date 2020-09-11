from django.db import models
from django import forms
from uuid import uuid4
import os

def min_length_3(value):
    if len(value) < 3:
        raise forms.ValidationError("3글자 이상 입력해주세요!")

def upload_to(instance, filename):
    path = 'file'
    uuid_name = uuid4().hex
    #확장자 뽑는거
    extension = os.path.splitext(filename)[-1].lower()
    #filename.split('.')[-1]
    return '/'.join([path, uuid_name + extension])

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=10, validators=[min_length_3])
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    file1 = models.FileField(null=True, blank=True, upload_to='')
    file2 = models.FileField(null=True, blank=True, upload_to=upload_to)
    img1 = models.ImageField(null=True, blank=True, upload_to='images/')
    img2 = models.ImageField(null=True, blank=True, upload_to='%Y/%m/%d')

class Scores(models.Model):
    name = models.CharField(max_length=10)
    math = models.IntegerField()
    english = models.IntegerField()
    science = models.IntegerField()