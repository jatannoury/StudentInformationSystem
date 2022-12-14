from urllib import request
from django.urls import path
from . import views
urlpatterns = [
    path('',views.getRoutes),
    path("sayHi/",views.sayHi),
    path("signUp/",views.signUp),
    path("logIn/",views.logIn),
    path("addCourse/",views.addCourse),
    path("addToAvailableCourses/",views.addToAvailableCourses),
    path("toggleRegistrationAccess/",views.toggleRegistrationAccess),
    path("getStudent/",views.getStudent),
    path("endSemester/",views.endSemester),
    # path("setStudentGrade/",views.setStudentGrade),
    # path("addInstructor/",views.addInstructor),
    
]