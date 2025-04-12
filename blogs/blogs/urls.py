from django.contrib import admin
from django.urls import path, include
from blog import urls as blogs_urls
from content import urls as content_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(blogs_urls)),
    path('', include(content_urls))
]
