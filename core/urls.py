from django.urls import path # type: ignore

from . import views
app_name = 'core'
urlpatterns = [
    path('', views.OnboardingSessionWizardView.as_view(), name='start'),
    path('get-started/', views.OnboardingSessionWizardView.as_view(), name='get-started'),
]
