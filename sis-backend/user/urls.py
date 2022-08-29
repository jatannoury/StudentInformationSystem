from urllib import request
from django.urls import path
from . import views
urlpatterns = [
    path('',views.getRoutes),
    path("searchCourse/",views.searchCourse),
    path("registerClass/",views.registerClass),
    
]