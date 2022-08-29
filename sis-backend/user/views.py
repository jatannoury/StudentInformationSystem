from django.contrib.auth.hashers import make_password,check_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Model.models import sisUser,availableCourses,courses
from Model.serializers import UserSerializer
from Model import serializers
import datetime
# import jwt
import json
# Create your views here.

#Helper Functions


@api_view(['GET'])
def getRoutes(request):
    routes=[
        'GET /api',
        'GET /api/searchCourse',
        
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
        
