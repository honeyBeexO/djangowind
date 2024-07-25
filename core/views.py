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
    "business": "forms/core/_business_.html",
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

    # def post(self, *args, **kwargs):
    #     # Handle "Back" navigation
    #     if 'wizard_goto_step' in self.request.POST:
    #         step = self.request.POST['wizard_goto_step']
    #         self.storage.current_step = step
    #         return self.render_form()

    #     # Handle form submission for the current step
    #     form = self.get_form(data=self.request.POST, files=self.request.FILES)
    #     if form.is_valid():
    #         print("Form is valid")
    #         # Save the form data in the session
    #         self.storage.set_step_data(self.steps.current, self.process_step(form))
    #         self.storage.set_step_files(self.steps.current, self.process_step_files(form))
    #         if self.steps.current == self.steps.last:
    #             return self.done(self.get_all_cleaned_data())
    #         else:
    #             return self.render_next_step(form.cleaned_data)
    #     else:
    #         print("Form is invalid:", form.errors)
    #         return self.render(form)

    # def render_form(self):
    #     """Render the form for the current step."""
    #     form = self.get_form()
    #     return self.render(self.get_context_data(form=form))
        
    # def get_form_step_data(self, step=None):
    #     if step is None:
    #         step = self.steps.current
    #     return self.storage.get_step_data(step) or {}
    
    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form=form, **kwargs)
        context['countries'] = core_models.Country.objects.all()
        return context



class OrderWizard(SessionWizardView):
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        #do_something_with_the_form_data(form_list)
        return HttpResponse('Onboarding process done')