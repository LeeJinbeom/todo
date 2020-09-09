from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('students', views.students, name='students'),
    path('students/<int:id>', views.students_detail, name='students'),
    path('scores', views.scores, name='scores')
    #path(URL경로 TEXT, views (함수들), 이름!)
]
