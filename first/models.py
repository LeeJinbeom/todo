from django.db import models
from django import forms

def min_length_3(value):
    if len(value) < 3:
        raise forms.ValidationError("3글자 이상 입력해주세요!")

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=10, validators=[min_length_3])
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=30)

class Scores(models.Model):
    name = models.CharField(max_length=10)
    math = models.IntegerField()
    english = models.IntegerField()
    science = models.IntegerField()