from .models import Posts
from django.forms import ModelForm

# This form is made from the Posts model
class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'post']