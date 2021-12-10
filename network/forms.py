from django import forms
from .models import *
from django.forms import TextInput

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ['dateTime', 'like', 'user']
        widgets = {
            'content': TextInput(attrs = {
                'class': "form-control"
            })
        }