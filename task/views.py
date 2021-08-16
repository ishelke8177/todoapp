from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import UserForm, TaskForm
from .models import Task
from django.urls import reverse_lazy

# Create your views here.

# Home Page
def todoView(request):

    user = request.user
    if user.is_authenticated:
        task_form = TaskForm()
        todos = Task.objects.filter(user=user).order_by('created_Date')
        return render(request,'task/task_list.html',{'task_form':task_form, 'todos':todos})
    else:
        return render(request,'task/task_list.html')


# Signup page
def signup(request):

    #registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            return HttpResponseRedirect(reverse('task:login'))
        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request,'task/signup.html',{'user_form':user_form})


# Login page
def userLogin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                auth_login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print('Someone tried to login')
            print("Username: {} and Password {}".format(username,password))
            return HttpResponse("Invalid Credentials")

    else:
        return render(request,'task/login.html')


@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse(todoView))


# About page
def aboutView(request):
    return render(request,'task/about.html')


# login
def loginView(request):
    return render(request,'task/login.html')
    

@login_required
def addTodo(request):
    user = request.user
    if user.is_authenticated:
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            todo = task_form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('home')
        else: 
            return render(request ,'task_list.html', context={'task_form' : task_form})
    else:
        pass


@login_required
def deleteTodo(request,pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('home')


@login_required
def updateTodo(request,pk):

    task = Task.objects.get(pk=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request,'task/update_task.html',{'form':form})


@login_required
def taskComplete(request,pk):

    task = Task.objects.get(pk=pk)
    task.completed = True
    task.save()

    return redirect('home')


@login_required
def completedTasks(request):

    user = request.user
    todos = Task.objects.filter(completed=True,user=user)

    return render(request,'task/completed_tasks_list.html',{'todos':todos})



