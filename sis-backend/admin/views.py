from rest_framework.decorators import api_view
from rest_framework.response import Response
from Model.models import sisUser
from Model.serializers import UserSerializer
from Model import serializers
import datetime
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

@api_view(["POST"])
def signUp(request):
    curr_year=str(datetime.date.today().year)
    users=sisUser.objects.filter(id__startswith=str(datetime.date.today().year)).values()
    newest_user_id=users[len(users)-1]['id'] if len(users)!=0 else 0000
    if str(newest_user_id)[0:4]==curr_year:
        new_user_id=newest_user_id+1
    else:
        new_user_id=curr_year+"0000"
    data=json.loads(request.body)
    newUser=sisUser(id=new_user_id,fname=data['fname'],email=data['email'],password=data['password'])
    newUser.save()
    return Response({'message':'succesful'})