from multiprocessing import context
from django.shortcuts import render,redirect,HttpResponse
from.forms import HomeForm
from. models import *
from django.contrib import messages
from django.views.generic import ListView

def index(request):
    return render(request,'index.html')
  

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

def authority(request):
    
    det=AuthorityModel.objects.all()
    context={
        'det':det

            } 
    return render(request,'authority.html',context)

# def staff(request):
#     table=ComplaintModel.objects.all()
#     return render(request,'staff.html',{'table':table})
class Staff(ListView):
    model=ComplaintModel
    template_name='staff.html'