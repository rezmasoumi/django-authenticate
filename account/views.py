from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from account.forms import LoginForm, EditProfileForm, ChangePasswordForm


def index(request):
    return render(request, 'account/index.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            field = form.cleaned_data
            user = authenticate(request, username=field['username'], password=field['password'])
            if user:
                login(request, user)
                return redirect('/dashboard')

        else:
            errors = form.errors
            return render(request, 'account/login.html', {'errors': errors})
    return render(request, 'account/login.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            return render(request, 'account/register.html')
    return render(request, 'account/register.html')


def dashboard(request):
    if request.user.is_authenticated:
        user = User.objects.get(username = request.user)
        return render(request, 'account/dashboard.html', {'username':user})
    else:
        return redirect('/login/')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/login/')

    else:
        return redirect('/login/')


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EditProfileForm(request.POST)
            if form.is_valid():
                user = User.objects.get(username=request.user)
                cd = form.cleaned_data
                user.email = cd['email']
                user.first_name = cd['first_name']
                user.last_name = cd['last_name']
                user.save()
                return redirect('/dashboard')

            return render(request, 'account/editprofile.html')
        return render(request, 'account/editprofile.html')
    return redirect('/login')


def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangePasswordForm(request.POST)
            if form.is_valid():
                print('1')
                cd = form.cleaned_data
                # if current user's password is same as old_password , return true
                user = request.user.check_password(cd['old_password'])
                if user:
                    if cd['new_password1'] == cd['new_password2']:
                        request.user.set_password(cd['new_password1'])
                        request.user.save()
                        return redirect('/login')
                return render(request, 'account/changepassword.html')

        return render(request, 'account/changepassword.html')

    return redirect('/login')

