from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes),
    path("sayHi/",views.sayHi),
    path("signUp/",views.signUp)
    
]