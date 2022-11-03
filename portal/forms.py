from cProfile import label
from random import choices
from django import forms
from .models import *

class HomeForm(forms.Form):
    # username=forms.CharField(label='Username',max_length=20, required=True)
    contact=forms.CharField(label='Contact No:',max_length=20, required=True)
    complaint=forms.CharField(label=' Complaint',max_length=200, required=True)
    coursename=forms.ModelChoiceField(queryset=CourseModel.objects.all(),empty_label="---Select District---",  required=True)

    # class HomeForm(forms.Form):
    # class Meta:
    #     Model=models.ComplaintModel
    #     fields="__all__"
class UserForm(forms.ModelForm):

    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password']
# class loginForm(forms.ModelForm):
    
#     class Meta:
#         model=User
#         fields=['username','password']





    