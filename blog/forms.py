from .models import Posts
from django.forms import ModelForm
from django import forms

# This form is made from the Posts model
class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'post']

# This form is made from the forms module imported on line 3
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=70, widget=forms.PasswordInput)