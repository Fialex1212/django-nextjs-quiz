from django.contrib.auth.forms import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateUserProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = []


class CreateQuiz(forms.ModelForm):
    tags = forms.CharField(required=False)
    class Meta:
        model = Quiz
        fields = ['title',  'tags']


class CreateQuestion(forms.ModelForm):
    class Meta:
        models = Question
        fields = ['Question', 'answer_1', 'answer_2', 'answer_3', 'answer_4']


