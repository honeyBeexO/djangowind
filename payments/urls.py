from django.urls import path # type: ignore

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
]