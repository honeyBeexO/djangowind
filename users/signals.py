# accounts/signals.py

from allauth.account.signals import user_logged_in # type: ignore
from django.dispatch import receiver # type: ignore

from django.conf import settings # type: ignore
from .models import Profile
from django.db.models.signals import post_save # type: ignore

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    # Perform your action here
    print(f'{user.email} logged in successfully.')
