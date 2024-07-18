from django.shortcuts import render # type: ignore
from core.forms import *
from formtools.wizard.views import SessionWizardView # type: ignore
from django.http import HttpResponse # type: ignore
# Create your views here.

class OnboardingSessionWizardView(SessionWizardView):
    form_list = [UserEntryInformationForm,UserPersonalInformationForm,UserBusinessActivityInformationForm,]
    template_name = 'onboarding.html'
    
    def done(self,form_list, **kwargs):
        return HttpResponse('Onboarding process done')