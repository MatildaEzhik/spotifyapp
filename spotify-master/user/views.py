from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_GET, require_POST

from user.forms import SignUpForm, SignInForm


# Create your views here.
def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home_page')
    sign_up_form = SignUpForm()
    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            # user_name = sign_up_form.cleaned_data['username']
            # password = sign_up_form.cleaned_data['password1']
            # user = authenticate(request, username=user_name, password=password)
            user = sign_up_form.save()
            login(request, user)

            return redirect('home_page')
    ctx = {
        'form': sign_up_form
    }

    return render(request, 'user/sign-up.html', context=ctx)


def sign_in(request):
    if request.user.is_authenticated:
        return redirect('home_page')
    sign_in_form = SignInForm()
    if request.method == 'POST':
        sign_in_form = SignInForm(request.POST)
        if sign_in_form.is_valid():
            user_name = sign_in_form.cleaned_data['username']
            password = sign_in_form.cleaned_data['password']
            user = authenticate(request, username=user_name, password=password)
            if user:
                login(request, user)
                return redirect('home_page')
    ctx = {
        'form': sign_in_form
    }
    return render(request, 'user/sign-in.html', context=ctx)


def check_user_permission(user):
    return user.is_superuser


@login_required(login_url='sign_up_page_name')
# @user_passes_test(check_user_permission, login_url='sign_in_page_name')
def profile(request):
    return render(request, 'user/profile.html')
