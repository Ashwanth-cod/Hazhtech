from django.shortcuts import render, redirect
from .models import *
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def blog_list(request):
    blogs = Blog.objects.all()
    blog_types = BlogType.objects.all()

    selected_types = request.GET.getlist('type')
    if selected_types:
        blogs = blogs.filter(type__id__in=selected_types).distinct()

    return render(request, 'blog_list.html', {
        'blogs': blogs,
        'blog_types': blog_types,
        'selected_types': selected_types,  # Pass selected types to the template
    })
    
def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'blog_detail.html', {'blog': blog})

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