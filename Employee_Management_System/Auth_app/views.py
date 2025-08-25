from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout


def Sign_Up(request):
    form = UserCreationForm()
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('log_in')
    template_name = 'Auth_app/sign_up.html'
    context = {'form':form}
    return render(request,template_name,context)

def Log_In(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        print(f"User is :- {user}")
        if(user is not None):
            login(request,user)
            return redirect('show_emp')
        return redirect('sign_up')
    template_name = 'Auth_app/log_in.html'
    context = {}
    return render(request,template_name,context)

def Log_Out(request):
    logout(request)
    return redirect('log_in')
