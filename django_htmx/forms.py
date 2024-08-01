from django import forms # type: ignore
from core.models import *
from django.utils.translation import gettext_lazy as _ # type: ignore

class SectorsForm(forms.Form):
    
    sector = forms.ModelChoiceField(
        empty_label='Choisir un secteur',
        queryset=Sector.objects.all(),
        initial= Sector.objects.get(sub_id=0),
        to_field_name="id",
        help_text='Choisir un secteur'
    )

class BusinessActivityForm(forms.ModelForm):
    activity_type = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=BusinessActivity.BUSINESS_CHOICES,
        label=_("Avez-vous déjà exercé une activité non-salariée ?"),
        initial=BusinessActivity.BUSINESS_CHOICES[0][0]
    )
    
    class Meta:
        model = BusinessActivity
        fields = ['sector','when_to_start','commercial_name','activity_type']
        widgets = {
            'sector': forms.Select(attrs={
                'placeholder': _("Domaine d'activité "),
                'label': _("Domaine d'activité "),
                }
            ),
            'when_to_start': forms.DateInput(attrs={'placeholder': _('DD-MM-YYYY'), 'type': 'date'}),
            'commercial_name': forms.TextInput(attrs={'placeholder': _('Nom comercial (optionnel)')}),
        }

        
