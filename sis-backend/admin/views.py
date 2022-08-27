from rest_framework.decorators import api_view
from rest_framework.response import Response
from Model.models import sisUser
from Model.serializers import UserSerializer
from Model import serializers
import json
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes=[
        'GET /api',
        'GET /api/sayHi',
    ]
    return Response(routes)

@api_view(['GET'])
def sayHi(request):
    return  Response("HI")