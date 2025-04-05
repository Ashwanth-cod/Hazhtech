from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Blog(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, editable=False)
    type = models.ManyToManyField('BlogType')  # Add ManyToManyField for types
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) + "-" + slugify(self.name)  # Use self.name
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title

class BlogType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
