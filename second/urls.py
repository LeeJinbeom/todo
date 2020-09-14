from . import views
from django.urls import path, include

app_name = 'second'

urlpatterns = [
    path('', views.index, name='index'),
    path('favourite', views.favourite, name='favourite'),
    path('favourite/<int:seq>', views.favourite_detail, name='favourite_detail'),
    path('favourite/add', views.favourite_add, name='favourite_add'),
    path('favourite/<int:seq>/modify', views.favourite_modify, name='favourite_modify'),
    path('favourite/<int:seq>/delete', views.favourite_delete, name='favourite_delete'),
    path('todo', views.todo, name='todo'),
    path('todo/<int:seq>', views.todo_detail, name='todo_detail'),
    path('todo/add', views.todo_add, name='todo_add'),
    path('todo/<int:seq>/modify', views.todo_modify, name='todo_modify'),
    path('todo/<int:seq>/delete', views.todo_delete, name='todo_delete'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout_view, name='logout'),
    path('favourite/<int:seq>/delete/ajax', views.favourite_delete_ajax, name='favourite_delete_ajax'),
]
