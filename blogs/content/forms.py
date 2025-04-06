from django import forms
from .models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'title', 'type', 'description', 'image']
    type = forms.ModelMultipleChoiceField(
        queryset=BlogType.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your comment...'}),
        }