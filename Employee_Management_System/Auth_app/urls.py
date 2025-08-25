from django.urls import path
from .views import ( Sign_Up,Log_In,Log_Out )

urlpatterns = [
    path('sign_up/',Sign_Up,name='sign_up'),
    path('log_in/',Log_In,name='log_in'),
    path('log_out/',Log_Out,name='log_out')
]