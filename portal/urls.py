from django.urls import path

from portal.views import *


urlpatterns = [
    path('complaint',complaint,name="complaint"),
    path('authority',authority,name="authority"),
    path('',index,name="index"),
    path('staff',Staff.as_view()),
    path('login',userlogin,name="login"),
    path('signup',createuser,name="signup"),
    path('logout',logoutFunction,name="logout")


   


]