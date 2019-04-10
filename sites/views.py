from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sites.forms import LoginForm,SignupForm


# Create your views here.

def signup(req):
    if req.user.username:
        return redirect(home)
    form = SignupForm()
    msg = ''
    if req.method == 'POST':
        form = SignupForm(req.POST)
        if form.is_valid():
            formData = form.cleaned_data
            user = User()
            user.username = formData['username']
            user.set_password(formData['password1'])
            user.email = formData['email']
            user.save()
            msg = 'User signup done successfully..!'
    return render(req, 'auth/signup.html', {'form': form, 'message': msg})


def signin(req):
    if req.user.username:
        return redirect(home)
    form = LoginForm()
    msg = ''
    if req.method == 'POST':
        form = LoginForm(req.POST)
        if form.is_valid():
            formDate = form.cleaned_data
            user = authenticate(
                username=formDate['username'],
                password=formDate['password']
            )
            if user is None:
                msg = 'Invalid login details..!'
            else:
                login(req, user)                # system define session/default session method
                req.session['city']='Bangalore' # User Define Session
                req.session['email'] = user.email
                return redirect(home)
    return render(req, 'auth/signin.html', {
        'form': form,
        'message': msg
    })


def home(req):
    return render(req, 'auth/home.html')


def sessionLogout(req):
    logout(req)
    return redirect(signin)
