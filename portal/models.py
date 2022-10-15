from django.db import models

# Create your models here.
class ComplaintModel(models.Model):
    name=models.CharField( max_length=50)
    complain=models.CharField( max_length=50)
    batch=models.CharField( max_length=50)
    contact=models.CharField( max_length=50)

    def __str__(self):
        return self.name

class AuthorityModel(models.Model):
    name=models.CharField( max_length=50)
    post=models.CharField( max_length=50)
    desc=models.CharField( max_length=150)
    contact=models.CharField( max_length=50)
    images=models.ImageField(upload_to='images')


    def __str__(self):
        return self.name


    


    

