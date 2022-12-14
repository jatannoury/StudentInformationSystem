from django.contrib.auth.hashers import make_password,check_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Model.models import sisUser,availableCourses,courses,registeredCourses
from Model.serializers import UserSerializer
from Model import serializers
import datetime
# import jwt
import json
# Create your views here.

#Helper Functions
def getAdmin():
    return sisUser.objects.filter(user_type=1).values()

@api_view(['GET'])
def getRoutes(request):
    routes=[
        'GET /api',
        'GET /api/searchCourse',
        'GET /api/registerClass',
        
    ]
    return Response(routes)

@api_view(["GET"])
def searchCourse(request):
    data=json.loads(request.body)
    all_courses=courses.objects
    if "code" in data:
        return Response(all_courses.filter(code=data['code']).values())    
    elif "title" in data:
        return Response(all_courses.filter(title=data['title']).values())    
    elif "faculty" in data:
        return Response(all_courses.filter(faculty=data['faculty']).values())    
    elif "department" in data:
        return Response(all_courses.filter(department=data['department']).values())    
    else:
        return Response(all_courses.all().values())    
        
@api_view(["POST"])
def registerClass(request):
    admin=getAdmin()
    if admin[0]['admin_allows_registration']==False:
        return Response({"message":"Not Registration period"})
    data=json.loads(request.body)
    sisUser.objects.filter(id=data['student_id']).update(is_registered_in_curr_sem=True)
    new_course_registered=registeredCourses(student_id=data['student_id'],registered_class_id=data['registered_class_id'],instructor_name=data['instructor_name'],time=data['time'],room=data['room'])
    available_course=availableCourses.objects.filter(id=data['registered_class_id'])
    available_course.update(available_seats=available_course.values()[0]['available_seats']-1,registered_seats=available_course.values()[0]['registered_seats']+1)
    new_course_registered.save()
    return Response({"message":"Succesful"})
    