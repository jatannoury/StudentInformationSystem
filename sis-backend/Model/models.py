from email.policy import default
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
from django.db import models

class sisUser(models.Model):
    id=models.CharField(primary_key=True,max_length=8)
    user_type=models.IntegerField(default=0)
    fname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    admin_allows_registration=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    is_registered_in_curr_sem=models.BooleanField(default=False)
    student_status=models.CharField(default="Not Registered",max_length=20)
    is_instructor=models.BooleanField(default=False)
    
    def __str__(self):
        return self.fname

class courses(models.Model):
    code=models.CharField(max_length=7)
    nb_of_credits=models.IntegerField()
    title=models.CharField(max_length=200)
    faculty=models.CharField(max_length=10)
    department=models.CharField(max_length=10)
    
    def __str__(self):
        return self.title
    
class availableCourses(models.Model):
    semester=models.CharField(max_length=12)
    code=models.CharField(max_length=12)
    instructor=models.CharField(max_length=200,default="Staff")
    room=models.CharField(max_length=20,default="TBA")
    registered_seats=models.IntegerField()
    available_seats=models.IntegerField()
    time=models.CharField(max_length=200)
    
    def __str__(self):
        return self.code


class registeredCourses(models.Model):
    student_id=models.CharField(max_length=12)
    registered_class_id=models.CharField(max_length=10)
    instructor_name=models.CharField(max_length=10)
    time=models.CharField(max_length=200)
    room=models.CharField(max_length=20)
    grade=models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(4.0)],default="0.00")
    
    def __str__(self):
        return self.student_id
    
