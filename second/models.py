from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True)
    # 여기다 추가해주세요~

class FavouriteGroup(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Favourite(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    memo = models.TextField()
    reg_date = models.DateField(auto_now_add=True)
    group = models.ForeignKey(FavouriteGroup, on_delete=models.CASCADE)
    reg_user = models.ForeignKey(User, on_delete=models.CASCADE)

class TodoGroup(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    reg_date = models.DateField(auto_now_add=True)
    del_yn = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Todo(models.Model):
    STATUS_CHOICE = (
        ('pending', '할일'),
        ('inporgress', '진행중'),
        ('end', '완료'),
    )
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    reg_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    del_yn = models.BooleanField(default=False)
    group = models.ForeignKey(TodoGroup, on_delete=models.CASCADE)
    reg_user = models.ForeignKey(User, on_delete=models.CASCADE)