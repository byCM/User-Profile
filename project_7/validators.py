from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class UserAttributeSimilarityValidator:

    def validate(self, newpass, user=None):
        if not user:
            return

        if user.username.lower() in newpass.lower():
            raise ValidationError(
                _("Password cannot contain username"),
                code='password_contains_username',
            )

        if hasattr(user, 'profile'):
            if user.first_name.lower() in newpass.lower():
                raise ValidationError(
                    _("Password cannot contain first name"),
                    code='password_contains_first_name',
                )

            if user.last_name.lower() in newpass.lower():
                raise ValidationError(
                    _("Password cannot contain last name"),
                    code='password_contains_last_name',
                )

    def get_help_text(self):
        return _("Password cannot contain username, first name, or last name.")