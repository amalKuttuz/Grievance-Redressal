from dataclasses import fields
from multiprocessing import context
from django.shortcuts import render,redirect,HttpResponse
from.forms import HomeForm,UserForm,Authorityfrom,ResponseUpdate
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
def viewcomplaints(request):
    username=request.user
    sq=ComplaintModel.objects.all()
    context={'sq':sq,'username':username}
    return render(request,'staff/complaints.html',context)

@login_required(login_url='login')
def staff(request):
    username=request.user
    context={'username':username}
    return render(request,'staff/staff.html',context)

@login_required(login_url='login')
def profile(request):
    user=request.user
    q=AuthorityModel.objects.get(user_id=user)
       
    form=Authorityfrom(instance=q)
    det=AuthorityModel.objects.filter(user_id=user)
    context={
        'det':det ,
        'form':form

            }  
    if request.method=='POST':
        form=Authorityfrom(request.POST,instance=q)
        if form.is_valid():
            form.save()
            det=AuthorityModel.objects.filter(user_id=user)
            context={
                'det':det ,
                'form':form

                    }  
            messages.success(request,"Profile Updated")
            return redirect('/profile')
        else:
            messages.error(request,"An error occured")

            return redirect('/profile')
    return render(request,'staff/profile.html',context)

@login_required(login_url='login')
def userlist(request):
    users=User.objects.all()
    context={'users':users}
    return render(request,'staff/userslist.html',context)


def logoutFunction(request):
    username=request.user
    if request.method=="POST":
        logout(request)
        messages.success(request, "sucessfully logged out")
        return redirect('/logout')
    return render(request,'auth/logout.html',{'username':username})


@login_required(login_url='login')
def responselist(request):
    res=ResponseModel.objects.all()
    context={'res':res}
    return render(request,'staff/response.html',context)

@login_required(login_url='login')
def updateresponse(request,id):
    q=ResponseModel.objects.get(id=id)
       
    form=ResponseUpdate(instance=q)
    context={
        'form':form

            }  
    if request.method=='POST':
        form=ResponseUpdate(request.POST,instance=q)
        if form.is_valid():
            form.save()
            context={
                'form':form

                    }  
            messages.success(request, "Response updated sucessfully")

            return redirect('/staff/response')
        else:
            messages.error("Unable to update")
            return redirect('/staff/response')


    return render(request,'staff/updateresponse.html',context)
def trackstatus(request):
    
        if request.method=='POST':
            s=ResponseModel.objects.filter(id=request.POST['Tracking'])
            context={
                "s":s
            }
            messages.success(request,"Status fetched sucessfully")
            return render(request,'user/trackstatus.html',context)
        else:
            context={
                "no":"no data to display"
            }
            messages.error(request,"Complaint not found")


        return render(request,'user/trackstatus.html',context)


def error_404_view(request, exception):
       
    # we add the path to the the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, '404.html')