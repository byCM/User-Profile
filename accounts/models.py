from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class ProfilePage(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    bio = models.CharField(max_length=255, validators=[MinLengthValidator(10)])
    email = models.EmailField(blank=True, null=True)
    avatar = models.ImageField(upload_to='images/', null=True, blank=True)
    user = models.OneToOneField(User, models.CASCADE)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        ProfilePage.objects.create(user=instance).save()


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profilepage.save()
