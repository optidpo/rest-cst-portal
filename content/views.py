from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django_daraja.mpesa.core import MpesaClient
from django.http import HttpResponse


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

        user = User.objects.create_user(username=username, email=email)
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

@login_required(login_url='login')
def myprofile(request, username):
    profile = User.objects.get(username=username)
    profile_details = Profile.objects.get(customer = profile.id)
    return render(request, 'myprofile.html', {'profile':profile, 'profile_details':profile_details})

@login_required(login_url='login')
def editprofile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if profile_form.is_valid():
           
            profile_form.save()
            messages.success(request, 'Your Profile Has Been Updated Successfully!')
            return redirect('myprofile', username=username)
        else:
            messages.error(request, "Your Profile Wasn't Updated!")
            return redirect('editprofile', username=username)
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'editprofile.html', {'user_form': user_form,'profile_form': profile_form})

login_required(login_url='login')
def addcard(request):
    form = AddCardInfo()
    if request.method == "POST":
        form = AddCardInfo(request.POST, request.FILES)
        if form.is_valid():
            card = form.save(commit=False)
            card.customer = request.user
            card.profile = request.user.profile
            card.save()
            messages.success(request, 'Your Card Information Was Added Successfully!')
            return redirect('myprofile')
        else:
            messages.error(request, "Your Card info  Wasn't Added!")
            return redirect('addcard')
    else:
        form = AddCardInfo()
    return render(request, 'addcard.html', {'form':form, })

def BuyGame(request, id):
    boughtGame =  Game.objects.get(id = id)
    currentUser = User.objects.get(id = request.user.id)

    neworder = Orders( customer = currentUser, game = boughtGame)
    if neworder:
        neworder.save()
        messages.success(request, "Game successfully added to cart")
        return redirect('index')


    else:
        messages.error(request, "Game was not successfully added to cart")
        return redirect('index')

def OrdersMade(request, username):
    currentUser = User.objects.get(username=username)
    gamesBought = Orders.objects.filter(customer=currentUser)
    if not gamesBought:
        messages.error(request, "You don't have any orders placed yet.")
    else:
        allGames = Game.objects.get(id=gamesBought)    
        return render(request, "orders.html", {'allGames':allGames, 'gamesBought':gamesBought })

def TopUpCard(request):
    cl = MpesaClient()
    phone_number = '0768951323'
    amount = 1
    account_reference = 'Amani Restaurant Online Gaming'
    transaction_desc = 'Amani Restaurant Online Gaming experience'
    callback_url = 'https://api.darajambili.com/express-payment'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)
    

              
  
 