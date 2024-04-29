from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import DocumentForm, SignupForm, LoginForm


# Create your views here.

def home(request):
    return render(request, 'home.html')


# login page
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


# signup page
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def forget_password(request):
    return render(request, 'forget_password.html')


# logout page
def logout(request):
    logout(request)
    return redirect('login')


def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
        else:
            return render(request, 'upload_document.html', {'form': form})
    else:
        form = DocumentForm()
    return render(request, 'upload_document.html', {'form': form})
