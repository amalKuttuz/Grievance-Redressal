from django.urls import path

from portal import views


urlpatterns = [
    path('',views.complaint,name="complaint"),
    path('authority',views.authority,name="authority"),


]