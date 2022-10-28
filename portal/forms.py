from cProfile import label
from random import choices
from django import forms
from .models import *

sq=CourseModel.objects.order_by('-id')

class HomeForm(forms.Form):
    # username=forms.CharField(label='Username',max_length=20, required=True)
    contact=forms.CharField(label='Contact No:',max_length=20, required=True)
    complaint=forms.CharField(label=' Complaint',max_length=200, required=True)
    # coursename=forms.ChoiceField(choices=sq, required=True)

    # class HomeForm(forms.Form):
    # class Meta:
    #     Model=models.ComplaintModel
    #     fields="__all__"






    