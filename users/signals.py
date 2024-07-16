# accounts/signals.py

from allauth.account.signals import user_logged_in # type: ignore
from django.dispatch import receiver # type: ignore

@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    # Perform your action here
    print(f'{user.email} logged in successfully.')
