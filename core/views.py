from django.shortcuts import render # type: ignore
from core.forms import *
from formtools.wizard.views import SessionWizardView # type: ignore
from django.http import HttpResponse # type: ignore
# Create your views here.
from django.utils.translation import gettext_lazy as _ # type: ignore


FORMS = [("contact", UserEntryInformationForm),
         ("information", UserPersonalInformationForm),
         ("business", UserBusinessActivityInformationForm),
         ("address", UserBusinessAddressInformationForm)]

TEMPLATES = {
    "contact": "forms/core/_contact.html",
    "information": "forms/core/_information.html",
    "business": "forms/core/_business.html",
    "address": "forms/core/_business.html"
    }

class OnboardingSessionWizardView(SessionWizardView):
    # form_list = [
    #     (_('CONTACT'),UserEntryInformationForm),
    #     (_('INFORMATIONS PERSONNELLES'),UserPersonalInformationForm),
    #     (_('VOTRE ACTIVITÉ '),UserBusinessActivityInformationForm), # Business Information
    #     ]
    # template_name = 'onboarding.html'
    form_list = FORMS
    
    def get_template_names(self):
        print(f"Current step: {self.steps.current}")
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        return HttpResponse('Onboarding process done')

    
    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form=form, **kwargs)
        context['countries'] = core_models.Country.objects.all()
        context['sectors'] = core_models.Sector.objects.all()
        context['sub_sectors'] = core_models.SubSector.objects.all()
        return context



class OrderWizard(SessionWizardView):
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        #do_something_with_the_form_data(form_list)
        return HttpResponse('Onboarding process done')