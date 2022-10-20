from enum import unique
from django.db import models

# Create your models here.
class ComplaintModel(models.Model):
    name=models.CharField( max_length=50)
    complain=models.CharField( max_length=50)
    batch=models.CharField( max_length=50)
    contact=models.CharField( max_length=50)
    # status=models.ForeignKey("portal.ResponseModel",on_delete=models.CASCADE)
    # reciept=models.ForeignKey("portal.ResponseModel",on_delete=models.CASCADE)

    def __str__(self):
        return self.complain

class AuthorityModel(models.Model):
    name=models.CharField( max_length=50)
    post=models.CharField( max_length=50)
    desc=models.CharField( max_length=150)
    contact=models.CharField( max_length=50)
    # images=models.ImageField(upload_to='images')


    def __str__(self):
        return self.name

class ResponseModel(models.Model):
    complain=models.ForeignKey("ComplaintModel",on_delete=models.CASCADE)
    status=models.CharField( max_length=100)
    reciept=models.CharField( max_length=300)


    def __str__(self):
        return self.status


    


    

