from django.utils.translation import gettext_lazy as _ # type: ignore
from users.managers import CustomUserManager
from django.contrib.auth.models import AbstractUser # type: ignore
from django.urls import reverse # type: ignore
from django.db.models import Model,CharField, EmailField,UUIDField,OneToOneField,ImageField,TextField,CASCADE # type: ignore
import uuid
from django.conf import settings # type: ignore

class CustomUser(AbstractUser):
    username = None
    name = CharField(_("Name of User"), blank=True, max_length=255)
    email = EmailField(_("email address"), unique=True)
    uuid = UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"uuid": self.uuid})
    
class Profile(Model):
    user = OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    full_name = CharField(max_length=255, blank=True, null=True)
    profile_image = ImageField(upload_to='profile_images/', blank=True, null=True)
    address = TextField(blank=True, null=True)
    uuid = UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.user.email
    
# from django.contrib.auth.models import AbstractUser
# from django.db.models import CharField
# from django.urls import reverse
# from django.utils.translation import gettext_lazy as _


# class User(AbstractUser):
#     """Default user for Google Auth."""

#     #: First and last name do not cover name patterns around the globe
#     name = CharField(_("Name of User"), blank=True, max_length=255)
#     first_name = None  # type: ignore
#     last_name = None  # type: ignore

#     def get_absolute_url(self):
#         """Get url for user's detail view.

#         Returns:
#             str: URL for user detail.

#         """
#         return reverse("users:detail", kwargs={"username": self.username})


# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from django.db import models
# from django.utils import timezone
# from django.utils.translation import gettext_lazy as _

# from .managers import CustomUserManager


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(_("email address"), unique=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(default=timezone.now)

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email