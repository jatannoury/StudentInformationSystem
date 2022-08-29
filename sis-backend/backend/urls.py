from django.contrib import admin
from django.urls import path, include

from admin import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/admin/',include('admin.urls')),
    path('api/user/',include('user.urls')),
]