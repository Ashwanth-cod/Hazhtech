from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Blogs(models.Model):
    name = models.CharField(max_length=100)  # Replace author with name
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    type = models.CharField(max_length=50, choices=[
        ('Tech', 'Tech'),
        ('Doubt', 'Doubt'),
    ])
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
