
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import ProfileCreationForm, ProfileChangeForm, ProfileLoginForm


def home(request):
    profile = request.user
    context = {}
    if profile.is_authenticated:
        full_name = f"{profile.first_name}-{profile.last_name}"
        context = {'full_name': full_name}
    return render(request, 'account/home.html', context)


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
    return render(request, 'account/signup.html',
                  {'signup_form': signup_form})


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
    return render(request, 'account/login.html',
                  {'login_form': login_form})


@login_required
def log_out(request):
    """
    Allow a logged in user to log out
    """
    logout(request)
    return redirect(settings.LOGIN_REDIRECT_URL)


@login_required
def update_account(request, full_name):
    """
    Allow a user to update his account
    """
    pass


@login_required
def account(request, full_name):
    """
    Allow a logged in user to access to his profile details
    """
    profile = request.user
    full_name = f"{profile.first_name}-{profile.last_name}"
    return render(request, 'account/account.html',
                  {'profile': profile, 'full_name': full_name})

