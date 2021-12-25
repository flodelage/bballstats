
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.urls import reverse

from .forms import ProfileCreationForm, ProfileChangeForm, ProfileLoginForm


def home(request):
    context = {'username': request.user.username} if request.user.is_authenticated else {}
    return render(
        request,
        'account/home.html',
        context
    )


def signup_page(request):
    """
    Allow a user to register an account
    """
    signup_form = ProfileCreationForm()
    if request.method == 'POST':
        signup_form = ProfileCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(
        request,
        'account/signup.html',
        {'signup_form': signup_form}
    )


def login_page(request):
    """
    Allow a user to log in
    """
    login_form = ProfileLoginForm()
    if request.method == 'POST':
        login_form = ProfileLoginForm(data=request.POST)
        if login_form.is_valid():
            user = authenticate(
                email=login_form.cleaned_data['email'],
                password=login_form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        login_form = ProfileLoginForm()
    return render(
        request,
        'account/login.html',
        {'login_form': login_form}
    )


@login_required
def log_out(request):
    """
    Allow a logged in user to log out
    """
    logout(request)
    return redirect(settings.LOGIN_REDIRECT_URL)


@login_required
def account(request, username):
    """
    Allow a logged in user to access to his profile details
    """
    return render(
        request,
        'account/account.html',
        {'profile': request.user, 'username': request.user.username}
    )


@login_required
def update_informations(request, username):
    if request.method == 'POST':
        update_form = ProfileChangeForm(request.POST, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            return redirect(
                reverse('account', kwargs={'username': request.user.username})
            )
    else:
        update_form = ProfileChangeForm(instance=request.user)
    return render(
        request,
        'account/update-informations.html',
        {'update_form': update_form, 'username': request.user.username}
    )


@login_required
def update_password(request, username):
    """
    Allow a user to update his account password
    """
    return render(
        request,
        'account/update-password.html',
        {'profile': profile, 'username': request.user.username}
    )
