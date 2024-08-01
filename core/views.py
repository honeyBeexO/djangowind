from django.shortcuts import render # type: ignore
from core.forms import *
from core.models import SubSector,Sector
from formtools.wizard.views import SessionWizardView # type: ignore
from django.http import HttpResponse, JsonResponse, HttpRequest # type: ignore
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
# def get_subsectors(request):
#     sector_id = request.GET.get('sector_id')
#     if sector_id:
#         subsectors = Sector.objects.get(id=sector_id).subsectors.all()#SubSector.objects.filter(parent_id=sector_id)
#         subsector_options = [{'id': sub.id, 'name': sub.name} for sub in subsectors]
#         print(f'JSON: {subsector_options} for {sector_id}')
#         return JsonResponse({'subsectors': subsector_options})
#     else:
#         print(f'JSON: [] for {sector_id}')
#     return JsonResponse({'subsectors': []})

def get_subsectors(request):
    sector_id = request.GET.get('sector_id')
    subsectors = []
    if sector_id:
        sector = Sector.objects.get(id=sector_id)
        subsectors = sector.subsectors.all()
    print(f'Loading subs for {sector_id}: {subsectors[:4]}')
    return render(request, 'partials/subsector_options.html', {'subsectors': subsectors})

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
        return context



class OrderWizard(SessionWizardView):
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        #do_something_with_the_form_data(form_list)
        return HttpResponse('Onboarding process done')