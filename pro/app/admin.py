from django.contrib import admin
from .models import My_Model

# Register your models here.


admin.site.register(My_Model)

class Admin(admin.ModelAdmin):
    list_display = ['title','product_name']