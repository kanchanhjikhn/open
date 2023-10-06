# chatapp/forms.py
from django import forms
from .models import Topic
from .models import Blog

class ChatForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['question']
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['topic', 'title', 'content', 'date']