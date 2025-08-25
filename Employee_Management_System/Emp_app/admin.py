from django.contrib import admin
from .models import Employee

# Register your models here.
@admin.register(Employee)
class Employee_admin(admin.ModelAdmin):
    list_display = ['eid','first_name','last_name','dept']