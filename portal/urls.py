from django.urls import path

from portal.views import *


urlpatterns = [
    path('complaint/',complaint,name="complaint"),
    path('authority/',authority,name="authority"),
    path('',index,name="index"),
    path('staff/',staff,name='staff'),
    path('complaints',viewcomplaints,name='complaints'),
    path('profile/',profile,name='profile'),

    path('login/',userlogin,name="login"),
    path('signup/',createuser,name="signup"),
    path('logout/',logoutFunction,name="logout"),
    path('staff/userslist',userlist,name="userslist"),
    path('staff/response',responselist,name="response")
    ,path('staff/response/<str:id>',updateresponse,name="updateresponse")
    ,path('track/',trackstatus,name="trackstatus")






   



]