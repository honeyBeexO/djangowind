from django import forms # type: ignore
from users.models import CustomUser
from django.utils.translation import gettext_lazy as _ # type: ignore
from django.core.validators import EmailValidator  # type: ignore
from users import models as user_models
from django.core.exceptions import ValidationError # type: ignore
from phonenumber_field.widgets import PhoneNumberPrefixWidget # type: ignore
from phonenumber_field.formfields import PhoneNumberField # type: ignore
from django.db.models import  TextChoices # type: ignore

class UserEntryInformationForm(forms.ModelForm):
    
    email_validator = EmailValidator(message=_('Invalid email format.'))
    def validate_email(value):
        allowed_domains = ['gmail.com', 'outlook.com', 'icloud.com', 'hotmail.com', 'live.com']
        email_domain = value.split('@')[-1].lower()
        if email_domain not in allowed_domains:
            raise ValidationError(_("Only Gmail, Outlook, iCloud, Hotmail, and Live email domains are allowed."))

    email = forms.EmailField(validators=[email_validator, validate_email])
    phone_number = PhoneNumberField()
    
    class Meta:
        model = user_models.CustomUser
        fields = (_('first_name'), _('last_name'),_('email'),_('phone_number'),) 
        
    def __init__(self, *args, **kwargs):
        super(UserEntryInformationForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].widget = PhoneNumberPrefixWidget(initial='FR')

class UserPersonalInformationForm(forms.ModelForm):
    pass
     

class UserBusinessActivityInformationForm(forms.ModelForm):
    pass 

class UserBusinessAddressInformationForm(forms.ModelForm):
    pass 
