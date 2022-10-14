from django.shortcuts import render,redirect,HttpResponse
from.forms import HomeForm
from. import models 
from django.contrib import messages



# Create your views here.
def complaint(request):
    if request.method=='POST':
        form=HomeForm(request.POST)

        if form.is_valid():
            datas=form.cleaned_data
            cd=models.ComplaintModel(
                name=datas['full_name'],
                complain=datas['complaint'],
                batch=datas['class_name'],
                contact=datas['contact']
                        )

            cd.save()
            messages.success(request,"Form submitted sucessfully")

    else:
        form=HomeForm()
    # return HttpResponse("pass")  
    return render(request,'complaint.html',{'form':form})