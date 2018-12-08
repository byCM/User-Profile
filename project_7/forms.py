from django import forms
from django.core.validators import EmailValidator
from django.forms import DateField, ModelForm, EmailField, ValidationError, Form, CharField, PasswordInput

from accounts.models import ProfilePage


class ProfileForm(ModelForm):
    class Meta:
        model = ProfilePage
        fields = ['first_name', 'last_name', 'dob', 'bio']


class EmailForm(ModelForm):
    email = EmailField()
    verify_email = EmailField(label='Confirm Email', validators=[EmailValidator()], required=False)

    class Meta:
        model = ProfilePage
        fields = ['email']

    def clean(self):
        cleaned_data = super(EmailForm, self).clean()
        email = cleaned_data['email']
        if email == self.instance.email:
            return
        try:
            verified_email = cleaned_data['verify_email']
        except KeyError:
            raise ValidationError('Emails must match!')
        if not email.lower() == verified_email.lower():
            raise ValidationError('Emails must match!')


class PasswordForm(Form):
    old_password = CharField(widget=PasswordInput, label='Current Password')
    new_password1 = CharField(widget=PasswordInput, label='New Password')
    new_password2 = CharField(widget=PasswordInput, label='Confirm New Password')

    def clean(self):
        current = self.cleaned_data['old_password']
        newpass = self.cleaned_data['new_password1']
        newpass2 = self.cleaned_data['new_password2']

        if newpass != newpass2:
            raise ValidationError("passwords do not match")
        else:
            print("That is current")

















