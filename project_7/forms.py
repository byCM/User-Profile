from django import forms
import re

from django.core.validators import EmailValidator
from django.forms import DateField, ModelForm, EmailField, ValidationError, Form, CharField, PasswordInput
from django.contrib.auth import get_user_model



from accounts.models import ProfilePage
from project_7.settings import DATE_INPUT_FORMATS


class ProfileForm(ModelForm):
    dob = DateField(input_formats=DATE_INPUT_FORMATS)

    class Meta:
        model = ProfilePage
        fields = ['avatar', 'first_name', 'last_name', 'dob', 'bio']


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
        cleaned_data = super().clean()
        current = cleaned_data['old_password']
        newpass = cleaned_data['new_password1']
        newpass2 = cleaned_data['new_password2']
        user = get_user_model()

        if user.username or user.first_name or user.last_name in newpass:
            raise ValidationError("Password cannot contain your username or name!")


        match = current == newpass
        match_new = newpass != newpass2
        length = not len(newpass) >= 14
        caps = newpass == newpass.upper() or newpass == newpass.lower()
        numerical = not re.search(r'\d', newpass)
        special = not re.search(r'\W', newpass)

        if match or match_new or length or caps or numerical or special:
            raise ValidationError('Please think of a new password, password must be:\n'
                                  'Different than your current password\n'
                                  '14 or more characters long\n'
                                  'Must have a capital letter and one or more numerical digits\n'
                                  'Must include a special character(@, #, $)\n'
                                  'Must not contain your username or your name\n')

