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
    return render(request, 'add.html', {'form':form, 'notification':notification})

def edit_task(request,pk):
    task = get_object_or_404(Tasks.objacts.all(), pk=pk)
    if request.method == 'POST':
        form = task_form(request.POST, instance=task)
        if form.is_valid():
            messages.success(request,'succesfully edited')
            form.save()
            return redirect('home')
        
    else:
        form = task_form()
    
    return render(request,'edit.html', )
    

def delete_task(request):
    pass

def completed(request):
    pass
