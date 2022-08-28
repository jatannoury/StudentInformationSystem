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
    # check for registered student having similar auto generated email
    while(sisUser.objects.filter(email=email).values()):
        print(email)
        similar_user_email=sisUser.objects.filter(email=email).values()
        if len(similar_user_email)!=0:
            email=email.split("@")
            registered_user_email=similar_user_email[0]['email'].split("@")
            registered_email_user_name=registered_user_email[0]
            try:
                int(registered_email_user_name[len(registered_email_user_name)-2:])
                new_user_code=int(registered_email_user_name[len(registered_email_user_name)-2:])
                if new_user_code<10:
                    email[0]=email[0][:len(email[0])-2]+"0"+str(new_user_code+1)
                    email=email[0]+email[1]
                else:
                    email[0]=email[0][:len(email[0])-2]+str(new_user_code)
                    email=email[0]+email[1]
                print(email)
            except:
                email[0]+="01"
                email=email[0]+"@"+email[1]
    newUser=sisUser(id=new_user_id,fname=data['fname'],email=email,password=make_password(data['password']))
    newUser.save()
    
    return Response({'message':'succesful'})