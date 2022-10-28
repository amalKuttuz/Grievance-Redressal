from email.policy import default
from enum import unique
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class AuthorityModel(models.Model):
    hod=models.CharField( max_length=50)
    post=models.CharField( max_length=50)
    desc=models.CharField( max_length=150)
    contact=models.CharField( max_length=50)
    images=models.ImageField(upload_to='images')


    def __str__(self):
        return self.hod

class DeptModel(models.Model):
        dept=models.CharField( max_length=50)
        hod=models.OneToOneField(AuthorityModel, on_delete=models.CASCADE)

        def __str__(self):
            return self.dept

class CourseModel(models.Model):
    coursename=models.CharField(max_length=100)
    dept=models.ForeignKey(DeptModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.coursename

# Create your models here.
class ComplaintModel(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    complaint=models.TextField()
    coursename=models.ForeignKey(CourseModel,on_delete=models.CASCADE)
    contact=models.IntegerField()
    createdon=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.complaint



class ResponseModel(models.Model):
    complaint=models.ForeignKey(ComplaintModel,on_delete=models.CASCADE)
    reciept=models.CharField( max_length=300)
    response=models.TextField()
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.response







    

