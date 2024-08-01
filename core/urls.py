from django.urls import path # type: ignore
from django.utils.translation import gettext_lazy as _ # type: ignore
from . import views
from . import forms
app_name = 'core'
urlpatterns = [
    path('', views.OnboardingSessionWizardView.as_view(views.FORMS), name='start'),
    path('get-subsectors/', views.get_subsectors, name='get-subsectors'),
    path('get-started/', views.OnboardingSessionWizardView.as_view(views.FORMS), name='get-started'),
]
