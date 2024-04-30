from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

from .forms import SignupForm, LoginForm, ChangePasswordForm


# Create your views here.

def home(request):
    return render(request, 'home.html')


# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('cyberapp:home_user')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cyberapp:login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('cyberapp:success')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })


def success(request):
    return render(request, 'success.html')


def forget_password(request):
    return render(request, 'forgot_password.html')


# logout page
def user_logout(request):
    logout(request)
    return redirect('login')


# @login_required
# def upload_file(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             document = form.save(commit=False)
#             document.user = request.user
#             document.save()
#             messages.success(request, "PDF Uploaded")
#         else:
#             return render(request, 'upload_document.html', {'form': form})
#     else:
#         form = DocumentForm()
#     return render(request, 'upload_document.html', {'form': form})
