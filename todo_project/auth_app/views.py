from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.
def SignUp(request):
    if request.method=='POST':
        auth_form = UserCreationForm(request.POST)
        if auth_form.is_valid():
            user = auth_form.save()
            login(request,user)
            return redirect('login')
    else:
        auth_form = UserCreationForm()

    return render(request,'registeration/login.html',{'auth_form':auth_form})