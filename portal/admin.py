from django.contrib import admin
from.models import AuthorityModel,ComplaintModel, ResponseModel

# Register your models here.
class AuthorityModels (admin.ModelAdmin):
    list_display=('name','desc','post','contact')
admin.site.register(AuthorityModel,AuthorityModels)

class Comp (admin.ModelAdmin):
    list_display=('name','complain','batch','contact')
admin.site.register(ComplaintModel,Comp)

class Res (admin.ModelAdmin):
    list_display=('complain','status','reciept')
admin.site.register(ResponseModel,Res)




