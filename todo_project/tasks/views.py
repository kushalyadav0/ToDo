from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import * # all
from .forms import * # all
# for authentication
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
 

# Create your views here.
# authentication views 
def signup(request):
    if request.method =='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form':form})


@login_required
def home(request):
    if User.is_authenticated():
        tasks = Tasks.objects.all() # get all items one by one
        return render(request, 'home.html', {'tasks':tasks}, )
    return redirect('signup')

@login_required
def add_task(request):
    form = task_form()
    if request.method =='POST':
        form = task_form(request.POST)
        if form.is_valid():
            notification = messages.success(request,"you've added task successfully")
            form.save()
            return redirect('home', ) # in redirect we use view and in render we use any_template.html
    else:
        form = task_form()
    return render(request, 'add.html', {'form':form})

@login_required
def edit_task(request,pk):
    task = get_object_or_404(Tasks.objects.all(), pk=pk)
    if request.method == 'POST':
        form = task_form(request.POST, instance=task.pk)
        if form.is_valid():
            messages.success(request,'succesfully edited')
            form.save()
            return redirect('home')
        
    else:
        form = task_form(request.GET)
    
    return render(request,'edit.html', {'form':form,'task':task})
    
@login_required
def delete_task(request, pk):
    task = get_object_or_404(Tasks,pk=pk)
    if request.method=='POST': 
        task.delete()
        return redirect('home')
    return render(request, 'delete.html', {'task':task})

@login_required
def completed(request,pk):
    task = get_object_or_404(Tasks,pk=pk)
    if request.method =='POST':
        task_c = task
        return(render(request,'home.html'))

    complete = True
    task_form.save
    return redirect('home')