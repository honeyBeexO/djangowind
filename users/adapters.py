from typing import Any

from allauth.account.adapter import DefaultAccountAdapter # type: ignore
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter # type: ignore
from django.conf import settings # type: ignore
from django.http import HttpRequest # type: ignore


class AccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request: HttpRequest):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request: HttpRequest, sociallogin: Any):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)
