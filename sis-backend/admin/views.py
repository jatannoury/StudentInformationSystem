from django.contrib.auth.hashers import make_password,check_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Model.models import sisUser,courses,availableCourses,registeredCourses
from Model.serializers import UserSerializer
from Model import serializers
import datetime
# import jwt
import json
# Create your views here.

#Helper Functions
def getAdmin():
    return sisUser.objects.filter(user_type=1).values()

def toggleRegistrationAccess():
    admin=getAdmin()
    sisUser.objects.filter(user_type=1).update(admin_allows_registration=not admin[0]['admin_allows_registration'])

def getInstructorCurrentCourses(instructor):
    curr_courses=availableCourses.objects.filter(instructor=instructor).values()
    return curr_courses

@api_view(['GET'])
def getRoutes(request):
    routes=[
        'GET /api',
        'GET /api/sayHi',
        'GET /api/signUp',
        'GET /api/logIn',
        'GET /api/getStudent',
        'POST /api/addCourse',
        'POST /api/toggleRegistrationAccess',
        'POST /api/addToAvailableCourses',
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

@api_view(['GET'])
def logIn(request):
    data=json.loads(request.body)
    user=sisUser.objects.filter(id=data['id']).values()
    if len(user)==0:
        return Response("Wrong Credentials")
    if check_password(data['password'],user[0]['password']):
        return Response(user) 
    return Response("Wrong Credentials")
        
@api_view(['POST'])
def addCourse(request):
    data=json.loads(request.body)
    new_course=courses(code=data['code'],nb_of_credits=data['nb_of_credits'],title=data['title'],faculty=data['faculty'],department=data['department'])
    new_course.save()
    return Response({"message":"Successful"})

    

@api_view(['POST'])
def addToAvailableCourses(request):
    data=json.loads(request.body)
    new_available_course=availableCourses(semester=data['semester'],code=data['code'],instructor=data['instructor'] if data["instructor"] else "Staff",registered_seats=data['registered_seats'],available_seats=data['available_seats'],time=data['time'])
    available_courses=availableCourses.objects.filter(code=data['code'])
    instructor_courses=getInstructorCurrentCourses(data['instructor'])
    for available_course in instructor_courses:
        if available_course['time']==data['time']:
            return Response({"message":"Instructor Is reserved for this timeline"})
        else:
            continue
    
    if available_courses:
        availableCourses.objects.filter(code=data['code']).update(semester=data['semester'],code=data['code'],instructor=data['instructor'] if data["instructor"] else "Staff",registered_seats=data['registered_seats'],available_seats=data['available_seats'],time=data['time'])
        return Response({'message':'Successful Update'})
        
    new_available_course.save()
    return Response({'message':'Successful'})

@api_view(['GET'])
def getStudent(request):
    users=sisUser.objects
    data=json.loads(request.body)
    if 'student_id' in data:
        return Response(users.filter(id=data['student_id']).values())
    elif 'fname' in data:
        return Response(users.filter(fname=data['fname']).values())
    elif 'email' in data:
        return Response(users.filter(email=data['email']).values())
    else:
        return Response(users.all().values())
    
    
@api_view(['DELETE'])
def endSemester(request):
    availableCourses.objects.all().delete()
    toggleRegistrationAccess()
    all_users=sisUser.objects.all().update(is_registered_in_curr_sem=False)
    
    return Response({"message":"Succesful"})
    