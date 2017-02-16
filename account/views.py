from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import RegisterForm, EditForm, LoginForm, PasswordForm


def login(request):
    if request.user.is_authenticated():
        return redirect('/')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def logout(request):
    if not request.user.is_authenticated():
        return redirect('/account/login')

    auth_logout(request)
    return render(request, 'account/logout.html')


def register(request):
    if request.user.is_authenticated():
        return redirect('/account/edit')

    form = RegisterForm(request.POST or None, prefix='user')
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/account/validation')
    return render(request, 'account/register.html', {'form': form})


def validation(request):
    return render(request, 'account/validation.html')


def edit(request):
    if not request.user.is_authenticated():
        return redirect('/account/login')

    form = EditForm(request.POST or None, prefix='user', instance=request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/account/edit')
    return render(request, 'account/edit.html', {'form': form})


def edit_password(request):
    if not request.user.is_authenticated():
        return redirect('/account/login')

    if request.method == 'POST':
        form = PasswordForm(request.user, data=request.POST, prefix='password')
        if form.is_valid():
            form.save()
            auth_login(request, request.user)
            return redirect('/account/edit')
    else:
        form = PasswordForm(request.user, prefix='password')
    return render(request, 'account/password.html', {'form': form})
