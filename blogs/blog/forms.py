from django import forms
from .models import Blog, BlogType, Comment  # Explicit imports for clarity

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'email', 'title', 'types', 'description', 'image']  # Corrected 'types'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blog Title'}),
            'type': forms.Select(attrs={'class': 'form-control', 'placeholder' : 'Select type'}),  # Allow multiple selections
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Blog Description'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your comment...'}),
        }
