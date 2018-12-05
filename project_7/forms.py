from django import forms
from django.forms import DateField, ModelForm

from accounts.models import ProfilePage


class ProfileForm(ModelForm):
    class Meta:
        model = ProfilePage
        fields = ['first_name', 'last_name', 'dob', 'bio']







