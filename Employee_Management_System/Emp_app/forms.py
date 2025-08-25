from django import forms
from .models import Employee

gender_choices = [
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
    ('OTHER','OTHER')
]

dept_choices = [
    ('HUMAN RESOURCES', 'HUMAN RESOURCES'),
    ('INFORMATION TECHNOLOGY', 'INFORMATION TECHNOLOGY'),
    ('FINANCE', 'FINANCE'),
    ('SALES', 'SALES'),
    ('MARKETING', 'MARKETING')
]

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'eid':'EMPLOYEE ID',
            'first_name':'FIRST NAME',
            'last_name':'LAST NAME',
            'city':'CITY',
            'gender':'GENDER',
            'phone_no':'PHONE NO',
            'address':'ADDRESS',
            'dept':'DEPARTMENT',
            'email_id':'EMAIL-ID',
            'password':'PASSWORD',
            'eligible':'ELIGIBILITY'
        }
        widgets = {
            'gender':forms.RadioSelect(choices=gender_choices),
            'dept':forms.Select(choices=dept_choices),
            'eid':forms.TextInput(attrs={
                'placeholder':'E.g.,101'
            }),
            'first_name':forms.TextInput(attrs={
                'placeholder':'Enter First Name',
            }),
            'last_name':forms.TextInput(attrs={
                'placeholder':'Enter Last Name',
            }),
            'city':forms.TextInput(attrs={
                'placeholder':'E.g.,Mumbai'
            }),
            'address':forms.Textarea(attrs={
                'rows':'3'
            }),
            'phone_no':forms.TextInput(attrs={
                'placeholder':'+91 ***** *****'
            }),
            'email_id':forms.TextInput(attrs={
                'placeholder':'********@gmail.com'
            }),
            'password':forms.PasswordInput(attrs={
                'type':'password'
            })
        }
