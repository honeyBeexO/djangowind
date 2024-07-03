from django.shortcuts import render

# Create your views here.
# payments/views.py

from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'