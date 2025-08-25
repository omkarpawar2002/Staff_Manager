from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=255)
    password = models.CharField(max_length=100)
    eligible = models.BooleanField(default=False)