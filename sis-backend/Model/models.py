from django.db import models

# Create your models here.
from django.db import models

class sisUser(models.Model):
    id=models.CharField(primary_key=True,max_length=8)
    fname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    isAdmin=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    
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
    code=models.ForeignKey(courses,on_delete=models.CASCADE)
    instructor=models.CharField(max_length=200)
    registered_seats=models.IntegerField()
    available_seats=models.IntegerField()
    time=models.CharField(max_length=200)
    
    def __str__(self):
        return self.fname
    
    