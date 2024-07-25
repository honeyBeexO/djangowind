from django.urls import path # type: ignore
from django.utils.translation import gettext_lazy as _ # type: ignore
from . import views
from . import forms
app_name = 'core'
urlpatterns = [
    # path('', views.OnboardingSessionWizardView.as_view( [
    #     (_('Contact Information'),forms.UserEntryInformationForm),
    #     (_('Personal Information'),forms.UserPersonalInformationForm),
    #     (_('Business Information'),forms.UserBusinessActivityInformationForm),
    #     ]), name='start'),
    path('', views.OnboardingSessionWizardView.as_view(views.FORMS), name='start'),
    # path('', views.TestSessionWizardView.as_view(
    #     [
    #     (_('Contact Information'),forms.UserEntryInformationForm),
    #     (_('Personal Information'),forms.UserPersonalInformationForm),
    #     (_('Business Information'),forms.UserBusinessActivityInformationForm),
    #     ]), name='start'),
    path('get-started/', views.OnboardingSessionWizardView.as_view(views.FORMS), name='get-started'),
]
