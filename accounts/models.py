from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class ProfilePage(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField()
    bio = models.CharField(max_length=255, validators=[MinLengthValidator(10)])
    email = models.EmailField()

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        ProfilePage.objects.create(user=instance)



