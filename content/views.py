from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
def index(request):
  games = Game.objects.all()  
  return render(request, "index.html", {'games':games})

def register(request):
  if request.method == 'POST':
        context = {'has_error': False}
        username = request.POST['username']        
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Passwords Do Not Match! Try Again')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username Already Exists! Choose Another One')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email Address Already Exists! Choose Another One')
            return redirect('register')
        
        # if User.objects.filter(phonenumber=phonenumber).exists():
        #   messages.error(request, 'Phone number already exists. Please enter another one' )
        #   return redirect('register')

        user = User.objects.create_user(username=username, email=email  )
        user.set_password(password1)
        user.save()        
  
  return render(request, 'register.html')

def loginUser(request):
  if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)     

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Username Does Not Exist! Choose Another One')
            return redirect('login')

        if user is None:
            messages.error(request, 'Username/Password Is Incorrect!! Please Try Again')
            return redirect('login')

        if user is not None:
            login(request, user)
            return redirect(reverse('index'))
  return render (request,'login.html')

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out!')
    return redirect('index')