from django.utils.translation import gettext_lazy as _ # type: ignore
from users.managers import CustomUserManager
from django.contrib.auth.models import AbstractUser # type: ignore
from django.urls import reverse # type: ignore
from django.db import models # type: ignore
import uuid
from django.conf import settings # type: ignore
from django.core.validators import RegexValidator # type: ignore
from phonenumber_field.modelfields import PhoneNumberField # type: ignore


from datetime import date

class Address(models.Model):
    name = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20, db_index=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='France')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Addresses"
        indexes = [
            models.Index(fields=['postal_code', 'city']),
        ]

    def __str__(self):
        return f"{self.name}, {self.street_address}, {self.postal_code} {self.city}, {self.country}"

    def formatted_address(self):
        return f"{self.name}\n{self.street_address}\n{self.postal_code} {self.city}\n{self.country}"

class PersonalInformation(models.Model):
    gender_choices =  [
             ('MALE', _('Man')),
             ('FEMALE', _('Woman')),
             ('OTHER', _('Other')),
            ]
    birth_country = models.CharField(max_length=100,blank=True, default=_('France'))
    birth_place = models.TextField(blank=True)
    birth_date = models.DateField(blank=True,default=date(1990,1,1))
    gender = models.CharField(max_length=20,blank=True,choices=gender_choices)
    
class CustomUser(AbstractUser):
    # phone_regex = RegexValidator(
    #     regex=r'^\+?1?\d{9,15}$', 
    #     message=_("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."),
    #                              )
    username = None
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(_("First name"), blank=True, max_length=255)
    last_name = models.CharField(_("Last name"), blank=True, max_length=255)
    email = models.EmailField(_("Email address"), unique=True)
    phone_number = PhoneNumberField(unique=True, max_length=16)
    # phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    home_address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_home_address')
    business_address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_business_address')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"uuid": self.uuid})

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.email