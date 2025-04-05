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
