from django import forms
from django.core.validators import MinLengthValidator

class ProfileForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=255)
    last_name = forms.CharField(label="Last Name", max_length=255)
    email = forms.EmailField()
    dob = forms.DateField()
    bio = forms.CharField(max_length=255, validators=[MinLengthValidator(10)])
    avatar = forms.ImageField(upload_to='/images/')
