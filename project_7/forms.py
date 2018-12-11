from django.core.validators import EmailValidator
from django.forms import DateField, ModelForm, EmailField, ValidationError
from django.contrib.auth.forms import PasswordChangeForm

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


class PasswordForm(PasswordChangeForm):
    pass
