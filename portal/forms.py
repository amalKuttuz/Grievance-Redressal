from cProfile import label
from random import choices
from django import forms
from .models import *

class HomeForm(forms.Form):
    # username=forms.CharField(label='Username',max_length=20, required=True)
    contact=forms.CharField(label='Contact No:',max_length=20, required=True)
    complaint=forms.CharField(label=' Complaint',max_length=200, required=True)
    coursename=forms.ModelChoiceField(queryset=CourseModel.objects.all(),empty_label="---Select Course---",  required=True)

    # class HomeForm(forms.Form):
    # class Meta:
    #     Model=models.ComplaintModel
    #     fields="__all__"
class UserForm(forms.ModelForm):
    # id=forms.IntegerField(=True)

    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password']
    
class Profileform(forms.ModelForm):
    # id=forms.IntegerField(=True)

    class Meta:
        model=User
        fields=['first_name','last_name','email','username']
    
class Authorityfrom(forms.ModelForm):

    class Meta:
        model=AuthorityModel
        fields=['hod',
        'post',
        'desc',
        'contact',
        'images']

class ResponseUpdate(forms.ModelForm):
    
    # response=forms.CharField(label=' Enter response to complaint',max_length=200, required=False)
    status=forms.ModelChoiceField(queryset=ResponseChoice.objects.all(),empty_label="---Select Status---",  required=True)

    class Meta:
        model=ResponseModel
        fields=['response','status']






    