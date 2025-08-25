from django.shortcuts import render,HttpResponse,redirect
from .forms import EmployeeForm
from .models import Employee
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='log_in')
def Add_Employee(request):
    form = EmployeeForm()
    if(request.method == 'POST'):
        form = EmployeeForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('show_emp')
    template_name = 'Emp_app/Add_emp.html'
    context = {'form':form}
    return render(request,template_name,context)

@login_required(login_url='log_in')
def Show_Employee(request):
    objs = Employee.objects.all()
    template_name = 'Emp_app/Show_emp.html'
    context = {'records':objs}
    return render(request,template_name,context)

def Update_Employee(request,pk):
    obj = Employee.objects.get(eid = pk)
    if(obj is not None):
        form = EmployeeForm(instance=obj) 
        if(request.method == 'POST'):
            form = EmployeeForm(request.POST,instance=obj)
            if(form.is_valid()):
                form.save()
                return redirect('show_emp')
    else:
        return HttpResponse("Object Is Not Found In Database")
    template_name = 'Emp_app/Update_emp.html'
    context = {'form':form}
    return render(request,template_name,context)

def Delete_Employee(request,pk):
    obj = Employee.objects.get(eid = pk)
    form = EmployeeForm()
    if(request.method == 'POST'):
        obj.delete()
        return redirect('show_emp')
    template_name = 'Emp_app/Delete_emp.html'
    context = {'obj':obj}
    return render(request,template_name,context)
