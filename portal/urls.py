from django.urls import path

from portal.views import *


urlpatterns = [
    path('complaint/',complaint,name="complaint"),
    path('authority/',authority,name="authority"),
    path('',index,name="index"),
    path('viewcomplaints/',viewcomplaints,name='viewcomplaints'),
    path('login/',userlogin,name="login"),
    path('signup/',createuser,name="signup"),
    path('logout/',logoutFunction,name="logout"),
        path('staff/userslist',userlist,name="userslist")



   



]