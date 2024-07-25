from django import forms # type: ignore
from django.utils.translation import gettext_lazy as _ # type: ignore
from django.core.validators import EmailValidator  # type: ignore
from users import models as user_models
from core import models as core_models
from django.core.exceptions import ValidationError # type: ignore
from phonenumber_field.widgets import PhoneNumberPrefixWidget # type: ignore
from phonenumber_field.formfields import PhoneNumberField,SplitPhoneNumberField # type: ignore
from django.db.models import  TextChoices # type: ignore
from django.utils import timezone # type: ignore

class UserEntryInformationForm(forms.ModelForm):
    
    email_validator = EmailValidator(message=_('Invalid email format.'))
    def validate_email(value):
        allowed_domains = ['gmail.com', 'outlook.com', 'icloud.com', 'hotmail.com', 'live.com']
        email_domain = value.split('@')[-1].lower()
        if email_domain not in allowed_domains:
            raise ValidationError(_("Only Gmail, Outlook, iCloud, Hotmail, and Live email domains are allowed."))

    email = forms.EmailField(required=True,validators=[email_validator, validate_email],help_text=_('john.doe@gmail.com'),widget=forms.EmailInput(attrs={'placeholder': 'john.doe@gmail.com','type':'email'}),)
    phone_number = PhoneNumberField(
        widget=forms.TextInput(
        attrs={'placeholder': '07000 123 456',
               'type':"tel",
               'title':_('Phone number format: 123-456-7890'),
               'aria-required':"true"
               }
            ),
        )
    
    class Meta:
        model = user_models.CustomUser
        fields = (_('first_name'), _('last_name'),_('email'), _('phone_number'),) 
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'John'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Doe'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(UserEntryInformationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True 
        #self.fields['phone_number'].widget = PhoneNumberPrefixWidget(initial='FR')

class UserPersonalInformationForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.TextInput(attrs={'placeholder': _('DD-MM-YYYY')}),
        input_formats=['%d-%m-%Y']
    )
    class Meta:
        model = user_models.PersonalInformation
        fields = (_('gender'),_('birth_date'),_('birth_country'),_('birth_place'),)
        widgets = {
            'gender': forms.Select(attrs={'placeholder': _('Select Gender')}),
            # 'birth_date': forms.DateInput(attrs={'placeholder': _('DD-MM-YYYY'), 'type': 'date'}),
            'birth_country': forms.TextInput(attrs={'placeholder': _('France')}),
            'birth_place': forms.TextInput(attrs={'placeholder': _('Saint denis, Paris')}),
        }
        
    def __init__(self, *args, **kwargs):
        super(UserPersonalInformationForm, self).__init__(*args, **kwargs)
        self.fields['birth_date'].required = True
        self.fields['birth_country'].required = True
        self.fields['birth_place'].required = True
        self.fields['gender'].required = True
        self.fields['gender'].initial = 'MALE'
        
        # Calculate the date that is 18 years ago from today
        today = timezone.now().date()
        eighteen_years_ago = today.replace(year=today.year - 18)
        self.fields['birth_date'].initial = eighteen_years_ago.strftime('%d-%m-%Y')
            # Debugging print statement
        print("Initial birth date value:", self.fields['birth_date'].initial)
     

class UserBusinessActivityInformationForm(forms.ModelForm):
    is_micro = forms.ChoiceField(
        choices=core_models.BusinessActivity.BUSINESS_CHOICES,
        widget=forms.RadioSelect,
        label= core_models.BusinessActivity.QUESTION2
    )
    class Meta:
        model = core_models.BusinessActivity
        fields = (_('sector'),_('sub_sector'),_('when_to_start'),_('commercial_name'),_('is_micro'))
        widgets = {
            'sector': forms.Select(attrs={
                'placeholder': _("Domaine d'activité "),
                'label': _("Domaine d'activité "),
                }
            ),
            'is_micro': forms.RadioSelect(attrs={
                'class': 'size-4 rounded border-gray-300',
                }
            ),
            
            'when_to_start': forms.DateInput(attrs={'placeholder': _('DD-MM-YYYY'), 'type': 'date'}),
            'commercial_name': forms.TextInput(attrs={'placeholder': _('Nom comercial (optionnel)')}),
            # 'birth_place': forms.TextInput(attrs={'placeholder': _('Saint denis, Paris')}),
        }

class UserBusinessAddressInformationForm(forms.ModelForm):
    pass 
