from django.contrib import admin
from.models import AuthorityModel,ComplaintModel, CourseModel, DeptModel, ResponseModel

# Register your models here.
class AuthorityModels (admin.ModelAdmin):
    list_display=('hod','desc','post','contact','images')
admin.site.register(AuthorityModel,AuthorityModels)

class Comp (admin.ModelAdmin):
    list_display=('username','complaint','coursename','contact')
admin.site.register(ComplaintModel,Comp)

class Res (admin.ModelAdmin):
    list_display=('complaint','reciept','response','status')
admin.site.register(ResponseModel,Res)

class Dep (admin.ModelAdmin):
    list_display=('dept','hod')
admin.site.register(DeptModel,Dep)

class Cor (admin.ModelAdmin):
    list_display=('coursename','dept')
admin.site.register(CourseModel,Cor)



