from . import views
from django.urls import path, include

app_name = 'second'

urlpatterns = [
    path('', views.index, name='index'),
    path('favourite', views.favourite, name='favourite'),
    path('favourite/<int:seq>', views.favourite_detail, name='favourite_detail'),
    path('favourite/add', views.favourite_add, name='favourite_add'),
    path('todo', views.todo, name='todo'),
    path('todo/<int:seq>', views.todo_detail, name='todo_detail'),
    path('todo/add', views.todo_add, name='todo_add'),
]
