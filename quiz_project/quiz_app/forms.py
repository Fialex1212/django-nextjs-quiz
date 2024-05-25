from django.contrib.auth.forms import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateUserProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = []


class CreateQuizForm(forms.ModelForm):
    tags = forms.CharField(required=False)
    class Meta:
        model = Quiz
        fields = ['title',  'tags']

    def __init__(self, *args, **kwargs):
        super(CreateQuizForm, self).__init__(*args, **kwargs)
        self.fields['tags'].required = False


class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['content', 'content_image']

    def __init__(self, *args, **kwargs):
        super(CreateQuestionForm, self).__init__(*args, **kwargs)
        self.fields['content_image'].required = False


class CreateAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content', 'content_image', 'is_correct']
    

    def __init__(self, *args, **kwargs):
        super(CreateAnswerForm, self).__init__(*args, **kwargs)
        self.fields['content_image'].required = False
        self.fields['is_correct'].required = False


#user forms
class ChangeUserNameForm(forms.Form):
    new_username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class ChangeUserEmailForm(forms.Form):
    new_email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class ChangeUserPasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput, required=True)
    new_password_repeated = forms.CharField(widget=forms.PasswordInput, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


    




