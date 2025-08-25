from django.urls import path
from .views import ( Add_Employee,Show_Employee,Update_Employee,Delete_Employee )

urlpatterns = [
    path('add_employee/',Add_Employee,name='add_emp'),
    path('show_employee/',Show_Employee,name='show_emp'),
    path('update_employee/<int:pk>/',Update_Employee,name='update_emp'),
    path('deplete_employee/<int:pk>/',Delete_Employee,name='delete_emp')
]