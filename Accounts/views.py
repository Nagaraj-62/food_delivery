from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password


# Create your views here.

def register(request):
    form=RegForm()
    if request.method == 'POST':
        form=RegForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('Accounts:login')
        else:
            print(form.errors)
            return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})
        
def user_login(request):
    form=LoginForm()
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user :
                login(request, user)
                return redirect('Restaurants:home')
            else:
                messages.error(request, 'Invalid username or password.')
                return render(request,'login.html',{'form':form})
    return render(request,'login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('Accounts:login')

@login_required(login_url='login')
def profile(request):
    user=request.user
    user_data=User_details.objects.filter(username=user)
    context={
        'user_data':user_data
    }
    return render(request,'profile.html',context)

@login_required(login_url='login')
def updateProfile(request):
    user=request.user
    form=RegForm(instance=user)
    if request.method == 'POST':
        form=RegForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('Accounts:profile')
        else:
            print(form.errors)
    return render(request,'updateProfile.html',{'form':form})

def contact(request):
    return render(request,'contact.html')