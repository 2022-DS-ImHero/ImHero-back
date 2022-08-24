from django.shortcuts import render

# Create your views here.
from contextlib import redirect_stdout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate
from django.contrib import auth
from .forms import UserCreationForm, LoginForm
# Create your views here.
def login(request):
    form = LoginForm(request=request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('mypage')
        return redirect('login')
    else:
        form = LoginForm()
        return render(request, 'login.html',{'form':form})

def logout(request):
    auth.logout(request)
    return redirect("main")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request,user)
            return redirect('mypage')
        return redirect('signup')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html',{'form':form})


def mypage(request):
    return render(request, 'mypage.html')