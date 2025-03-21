from django.shortcuts import render, redirect, get_object_or_404
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
            return redirect('home', ) # in redirect we use view and in render we use any_template.html
    else:
        form = task_form()
    return render(request, 'add.html', {'form':form})

def edit_task(request,pk):
    task = get_object_or_404(Tasks.objects.all(), pk=pk)
    if request.method == 'POST':
        form = task_form(request.POST, instance=task)
        if form.is_valid():
            messages.success(request,'succesfully edited')
            form.save()
            return redirect('home')
        
    else:
        form = task_form(request.POST)
    
    return render(request,'edit.html', {'form':form,'task':task})
    
def delete_task(request, pk):
    task = get_object_or_404(Tasks,pk=pk)
    if request.method=='POST':
        task.delete()
        return redirect('home')
    return render(request, 'delete.html', {'task':task})

def completed(request,pk):
    task = get_object_or_404(Tasks,pk=pk)
    complete = True
    task_form.save
    return redirect('home')