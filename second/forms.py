from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Favourite, Todo, User

class SignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = '패스워드'
        self.fields['password2'].label = '패스워드확인'
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'phone_number']
        labels = {
            'username': '아이디',
            'email': '이메일',
            'phone_number': '핸드폰번호',
            #'password': '패스워드'
        }


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages['invalid_login'] = '아이디, 패스워드를 확인해주세요'

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password']


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