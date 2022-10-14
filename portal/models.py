from django.db import models

# Create your models here.
class ComplaintModel(models.Model):
    name=models.CharField( max_length=50)
    complain=models.CharField( max_length=50)
    batch=models.CharField( max_length=50)
    contact=models.CharField( max_length=50)

    def __str__(self):
        return self.name

    


    

