from django.contrib import admin
from .models import employee,department
# Register your models here.


# Register your models here.
#admin.site.register(employee)
@admin.register(employee)
class employee(admin.ModelAdmin):
    list_display=['id','ename','empid','email','password','mobile','dep']

@admin.register(department)
class department(admin.ModelAdmin):
    list_display=['id','dept']