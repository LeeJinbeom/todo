from django import forms
from .models import Favourite, Todo

class FavouriteModelForm(forms.ModelForm):

    class Meta:
        model = Favourite
        fields = ['name', 'url', 'memo', 'group']
        labels = {
            'name': '이름',
            'url': 'URL',
            'memo': '메모',
            'group': '카테고리'
        }

class TodoModelForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['name', 'status', 'end_date', 'group']
        labels = {
            'name': '이름',
            'status': '상태',
            'end_date': '종료일',
            'group': '카테고리'
        }