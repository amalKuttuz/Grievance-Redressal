from cProfile import label
from django import forms

class HomeForm(forms.Form):
    full_name=forms.CharField(label='Full Name:',max_length=20, required=True)
    contact=forms.CharField(label='Contact No:',max_length=20, required=True)
    complaint=forms.CharField(label=' Complaint',max_length=200, required=True)
    class_name=forms.CharField(label=' Class/Batch',max_length=20, required=True)

    # class HomeForm(forms.Form):
    # class Meta:
    #     Model=models.ComplaintModel
    #     fields="__all__"






    