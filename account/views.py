
from django.shortcuts import render

from .forms import ProfileCreationForm, ProfileChangeForm


def home(request):
    return render(request, 'account/home.html', {})

def signup(request):
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
                  context = {'signup_form': signup_form})

