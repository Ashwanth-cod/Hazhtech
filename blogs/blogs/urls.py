from django.contrib import admin
from django.urls import path, include  # Import include
from content import urls as blogs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(blogs_urls)),  # Use include() to link the app's URLs
]
