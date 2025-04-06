from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import BlogForm
from .forms import CommentForm  # Ensure the form is imported
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def blog_list(request):
    selected_type = request.GET.get("type", "")
    print(f"Selected Type: {selected_type}")  # Debugging line

    blogs = Blog.objects.all()
    blog_types = BlogType.objects.all()

    if selected_type:
        blogs = blogs.filter(types__id=selected_type)  # Filtering correctly

    return render(request, "blog_list.html", {
        "blogs": blogs,
        "blog_types": blog_types,
        "selected_types": selected_type,
    })


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        content = request.POST.get("content")

        if name and email and content:
            Comment.objects.create(blog=blog, name=name, email=email, content=content)

    comments = blog.comments.all().order_by("-created_at")  # Fetch comments

    return render(request, "blog_detail.html", {"blog": blog, "comments": comments})
    
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
