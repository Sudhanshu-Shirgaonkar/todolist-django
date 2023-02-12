from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import TaskForm
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.forms import UserCreationForm  
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.



def userLogin(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully Logged In')
            return redirect('index')
        
        else:
        # Return an 'invalid login' error message.
        
            messages.error(request,'Please enter correct username or password!')
            

    context = {'page':page}

    return render(request,'base/login_register.html',context)



def logoutUser(request):
    logout(request)
    return redirect('login')



def register(request):
    page = 'register'
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():
            
            
            user = form.save(commit=False)

            user.username = user.username.lower()

            try:

                if User.objects.get(username__iexact = user.username):
                    messages.error(request,'A user with that username already exists.')
                    return redirect('register')

            except User.DoesNotExist:
        

                user.save()
                messages.success(request, 'Account created Successfully . Please LogIn')
                return redirect('login')

        else:
            
            # messages.error(request,form.errors.values())

            for err in form.errors.values():
                messages.error(request,err)
                
         


    form = UserCreationForm()

    context = {'form':form,'page':page} 

    return render(request,'base/login_register.html',context)
        



@login_required(login_url='login')
def index(request):

    form = TaskForm()
    tasks = Task.objects.all().filter(user = request.user)

    count = Task.objects.all().filter(complete = False,user = request.user).count()

    if request.method == 'POST':


        form = TaskForm(request.POST)

        if form.is_valid():
            
            task = form.save(commit=False)

            task.user = request.user
            task.save()


        return redirect('index')

    context = {'form':form,'tasks':tasks,'count':count}
    return render(request,'base/index.html',context)



def update(request,pk):

    task = Task.objects.get(id = pk)
    form = TaskForm(instance= task) 

    if request.method == 'POST':
        form = TaskForm(request.POST,instance= task) 

        if form.is_valid():
            task = form.save()
            task.user = request.user
            task.save()
            messages.info(request,'Task Updated')
            return redirect('index')
     
    context = {'form':form}
    return render(request,'base/update.html',context)


def delete(request,pk):

    task = Task.objects.get(id = pk)
    if request.method == 'POST':
        task.delete()
        messages.warning(request, 'Task deleted.')
        return redirect('index')

    return render(request,'base/delete.html')

