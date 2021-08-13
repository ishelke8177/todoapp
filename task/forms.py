from django import forms
from django.contrib.auth import models
from django.contrib.auth.models import User
from .models import Task


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username','email','password')


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}),label='')
    class Meta:
        model = Task
        fields = ('title',)