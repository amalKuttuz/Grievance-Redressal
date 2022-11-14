from email.policy import default
from enum import unique
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class AuthorityModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    hod=models.CharField( max_length=50,null=True)
    post=models.CharField( max_length=50,null=True)
    desc=models.CharField( max_length=150,null=True)
    contact=models.CharField( max_length=50,null=True)
    images=models.ImageField(upload_to='images',null=True)


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

class ResponseChoice(models.Model):
    status=models.CharField(max_length=50)

    def __str__(self):
        return self.status

class ResponseModel(models.Model):
    complaint=models.ForeignKey(ComplaintModel,on_delete=models.CASCADE)
    response=models.TextField()
    status=models.ForeignKey(ResponseChoice, on_delete=models.CASCADE)

    def __str__(self):
        return self.response


    





    

