from django.contrib import admin
from.models import AuthorityModel,ComplaintModel

# Register your models here.
class AuthorityModels (admin.ModelAdmin):
    list_display=('name','desc','post','contact','images')
admin.site.register(AuthorityModel,AuthorityModels)

class Comp (admin.ModelAdmin):
    list_display=('name','complain','batch','contact')
admin.site.register(ComplaintModel,Comp)


