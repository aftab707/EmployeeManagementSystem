from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def home_page(request):

    return render(request, 'home.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid Username")
            return redirect('/login/')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.info(request, "Password is Incorrect")
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/home/')
     
    return render(request, 'login.html')


def register_page(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not username or not password:
            messages.info(request, "Username or Password missed")
            return redirect('/register/')
        

        if User.objects.filter(username = username).exists():
            messages.info(request, "Username already exist ")
            return redirect('/register/')
        
        user = User.objects.create(username = username)
        user.set_password(password)
        user.save()

        messages.info(request, "Account Created Successfully ")
        return redirect('/login/')
    
     
    return render(request, 'register.html')



@login_required(login_url='/login/')
def dashboard_page(request):

    queryset = Employee.objects.all()
    context = {'employees':queryset}
    return render(request, 'dashboard.html', context)


@login_required(login_url='/login/')
def singleemployee_page(request, id):
    queryset = Employee.objects.get(id = id)
    context = {'employees':queryset}
     
    return render(request, 'singleemploye.html', context)


@login_required(login_url='/login/')
def udateemployee_page(request , id):
    queryset = Employee.objects.get(id = id)
    context = {'emp':queryset}
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        email = data.get('email')
        phone = data.get('phone')
        address = data.get('address')
        
        
        
        queryset.user.username = username
        queryset.user.email = email
        queryset.user.save()
        queryset.phone = phone
        queryset.address = address
        queryset.save()
        messages.info(request, "User Data Updated")
     
    return render(request, 'updateemployee.html', context)



@login_required(login_url='/login/')
def addnewemp_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose a different one.")
            return redirect('/addnewemployee/')
        
        user = User.objects.create(username = username, email = email)

        Employee.objects.create(
            user = user,
            phone = phone,
            address = address
        )
        messages.info(request, "Employee Added")
        return redirect('/addnewemployee/')


    return render(request, 'addnewemployee.html')



@login_required(login_url='/login/')
def delete_emp(request, id):
    queryset = Employee.objects.get(id = id)
    queryset.user.delete()
    return redirect('/dashboard/')



@login_required(login_url='/login/')
def logout_page(request):
    logout(request)
    return redirect('/login/')