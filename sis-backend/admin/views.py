from django.contrib.auth.hashers import make_password
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
    all_users=sisUser.objects.all()
    # Auto generate user id
    curr_year=str(datetime.date.today().year)
    curr_year_users=sisUser.objects.filter(id__startswith=str(datetime.date.today().year)).values()
    newest_user_id=curr_year_users[len(curr_year_users)-1]['id'] if len(curr_year_users)!=0 else 0000
    if str(newest_user_id)[0:4]==curr_year:
        new_user_id=int(newest_user_id)+1
    else:
        new_user_id=curr_year+"0000"
    data=json.loads(request.body)
    # Auto generate user email
    fname=str(data['fname']).split(" ")
    email=""
    for i in range(len(fname)):
        if i==len(fname)-1:
            fname[i]=fname[i].lower()
            email+=fname[i]
            continue
        fname[i]=fname[i].lower()[0]
        email+=fname[i]
    email+="@university.com"
    newUser=sisUser(id=new_user_id,fname=data['fname'],email=email,password=make_password(data['password']))
    newUser.save()
    return Response({'message':'succesful'})