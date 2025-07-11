from django.shortcuts import render, redirect, get_object_or_404
from .models import * # all
from .forms import * # all
# for authentication
from django.contrib.auth import login
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
    if User.is_authenticated:
        tasks = Tasks.objects.filter(user=request.user) # get all items one by one
        return render(request, 'home.html', {'tasks':tasks,})
    else:
        return redirect('login')


@login_required
def add_task(request):
    form = task_form()
    if request.method =='POST':
        form = task_form(request.POST)
        if form.is_valid(): 
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home', ) # in redirect we use view and in render we use any_template.html
    else:
        form = task_form()
    return render(request, 'add.html', {'form':form})
    
    
@login_required
def edit_task(request,pk):
    task = get_object_or_404(Tasks, pk=pk, user = request.user)
    if request.method == 'POST':
        form = task_form(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = task_form(request.GET)
    
    return render(request,'edit.html', {'form':form,'task':task})
    
@login_required
def delete_task(request, pk):
    task = get_object_or_404(Tasks,pk=pk, user = request.user)
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