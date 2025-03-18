from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Tasks
from .forms import task_form


# Create your views here.
def home(request):
    tasks = Tasks.objects.all() # get all items one by one
    return render(request, 'home.html', {'tasks':tasks}, )

def add_task(request):
    form = task_form()
    if request.method =='POST':
        form = task_form(request.POST)
        if form.is_valid():
            notification = messages.success(request,"you've added task successfully")
            form.save()
            return redirect('home')
    else:
        form = task_form()
    return render(request, 'add.html', {'form':form, 'notification':notification})

def task(request):
    pass

def edit_task(request):
    pass

def delete_task(request):
    pass

def completed(request):
    pass
