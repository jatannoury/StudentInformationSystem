from django.contrib.auth.hashers import make_password,check_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Model.models import sisUser,courses,availableCourses
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
        
    ]
    return Response(routes)

