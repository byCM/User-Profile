from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User

from .forms import ProfileForm, EmailForm, PasswordForm
from accounts.models import ProfilePage


def home(request):
    return render(request, 'home.html')


def profile_view(request):
        profile = ProfilePage.objects.get(user=request.user)
        return render(request, 'accounts/profile.html', {'profile': profile})


@login_required
def edit_profile(request):
    profile = ProfilePage.objects.get(user=request.user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profilepage, files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            return HttpResponseRedirect(reverse('profile'))
        return render(request, 'accounts/edit_profile.html', {'profile_form': profile_form})
    profile_form = ProfileForm(instance=profile)
    return render(request, 'accounts/edit_profile.html', {'profile_form': profile_form})


@login_required
def change_email(request):
    email = ProfilePage.objects.get(user=request.user)

    if request.method == "POST":
        email_form = EmailForm(request.POST, instance=request.user.profilepage)
        if email_form.is_valid() and email_form.cleaned_data['email'] == email_form.cleaned_data['verify_email']:
            email_form.save()
            return HttpResponseRedirect(reverse('profile'))
        return render(request, 'accounts/change_email.html', {'email_form': email_form})
    email_form = EmailForm(instance=email)
    return render(request, 'accounts/change_email.html', {'email_form': email_form})


@login_required
def change_password(request):
    user = request.user
    profile = ProfilePage.objects.get(user=request.user)

    if request.method == 'POST':
        password_form = PasswordForm(request.POST)
        if password_form.is_valid():
            old_password = password_form['old_password']
            new_password = password_form['new_password1']
            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()
                messages.success(request, "Your password has been changed")
            else:
                messages.success(request, "That is not your current password")
                return HttpResponseRedirect(reverse('profile'))
        return render(request, 'accounts/change_password.html', {'password_form': password_form})
    password_form = PasswordForm()
    return render(request, 'accounts/change_password.html', {'password_form': password_form})

