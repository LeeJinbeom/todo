from . import views
from django.urls import path, include

app_name = 'first'

urlpatterns = [
    path('', views.index, name='index'),
    path('students', views.students, name='students'),
    path('students/add', views.student_add, name='student_add'),
    path('students/modify/<int:id>', views.student_modify, name='student_modify'),
    path('students/<int:id>', views.students_detail, name='students'),
    path('scores', views.scores, name='scores'),
    path('scores/add', views.score_add, name='scores_add'),
    path('makecookie/<name>', views.make_cookie, name='make_cookie')
    #path(URL경로 TEXT, views (함수들), 이름!)
]
