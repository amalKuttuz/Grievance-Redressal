from dataclasses import fields
from multiprocessing import context
from django.shortcuts import render,redirect,HttpResponse
from.forms import HomeForm,UserForm
from. models import *
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.models import Permission, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login,authenticate
from django.contrib import messages


def index(request):
    return render(request,'user/index.html')

def createuser(request):
    forms=UserForm()   
    if request.method=='POST':
        forms=UserForm(request.POST)   
        if forms.is_valid():
            forms.save()
            messages.success(request,"Account created sucessfully")

            return redirect('/')
        else:
            messages.error(request,"error")

            return render(request,'auth/signup.html',{'forms':forms})

    return render(request,'auth/signup.html',{'forms':forms})


def userlogin(request):
  
    if request.method=='POST':
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            login(request,user)
            return render(request,'user/index.html')

        else:
            messages.error(request,"Incorrect credentials")

            return render(request,'auth/login.html')

    return render(request,'auth/login.html')



# Create your views here.
@login_required(login_url='login')
def complaint(request):
    

    if request.method=='POST':
        form=HomeForm(request.POST)
        
        if form.is_valid():
            
            datas=form.cleaned_data
            cd=ComplaintModel(
                username=request.user,
                complaint=datas['complaint'],
                coursename=datas['coursename'],
                contact=datas['contact']
                        )

            cd.save()
            messages.success(request,"Complaint submitted sucessfully")

    else:
        form=HomeForm()

    return render(request,'user/complaint.html',{'form':form})

def authority(request):
    
    det=AuthorityModel.objects.all()
    context={
        'det':det

            } 
    return render(request,'user/authority.html',context)

@login_required(login_url='login')
def staffs(request):
    sq=ComplaintModel.objects.all()
    context={'sq':sq}
    return render(request,'staff/staff.html',context)


def logoutFunction(request):
    username=request.user
    if request.method=="POST":
        logout(request)
        messages.success(request, "sucessfully logged out")
        return redirect('/')
    return render(request,'auth/logout.html',{'username':username})
    