from django.shortcuts import render, redirect
from .models import Blogs
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def blog_list(request):
    blogs = Blogs.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})

def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)  # Do not save to the database yet
            blog.save()  # Now save it to the database
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog_form.html', {'form': form})