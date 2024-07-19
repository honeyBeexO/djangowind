from django.shortcuts import render # type: ignore
from core.forms import *
from formtools.wizard.views import SessionWizardView # type: ignore
from django.http import HttpResponse # type: ignore
# Create your views here.
from django.utils.translation import gettext_lazy as _ # type: ignore
class OnboardingSessionWizardView(SessionWizardView):
    form_list = [
        (_('Contact Information'),UserEntryInformationForm),
        (_('Personal Information'),UserPersonalInformationForm),
        (_('Business Information'),UserBusinessActivityInformationForm),
        ]
    template_name = 'onboarding.html'
    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form=form, **kwargs)
        context['steps'] = self.get_form_list()
        context['current_step'] = self.steps.current
        context['step_index'] = list(self.get_form_list().keys()).index(self.steps.current)
        return context
    
    def done(self,form_list, **kwargs):
        return HttpResponse('Onboarding process done')