from django import forms
from .models import *

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['title','content','image',
                'category','published_date']