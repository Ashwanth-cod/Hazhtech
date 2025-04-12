from django.contrib import admin
from .models import *

admin.site.register(Blog)   
admin.site.register(BlogType)
admin.site.register(Comment)