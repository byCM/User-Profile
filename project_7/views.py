from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from . import forms

from .forms import ProfileForm
from accounts.models import ProfilePage

def home(request):
    return render(request, 'home.html')

def profile_view(request):
        return render(request, 'accounts/profile.html', {'user': request.user})

@login_required
def edit_profile(request):
    profile = ProfilePage.objects.get(user=request.user)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profilepage, files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            return HttpResponseRedirect(reverse('profile'))
        return render(request, 'accounts/edit_profile.html', {'profile_form': profile_form})
    return render(request, 'accounts/edit_profile.html')

