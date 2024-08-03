from django.shortcuts import render,get_object_or_404 # type: ignore
from django.core.serializers import serialize # type: ignore
from core.models import *
from .forms import *
from django.http import JsonResponse, HttpResponse # type: ignore
# Create your views here.


def index(request):
    form = BusinessAddressForm()
    return render(request, 'tests/htmx_test.html', {'form': form})

def get_subsectors(request):
    subsectors = []
    print(f'GET request data: {request.GET}')
    sector_id =  request.GET.get('sector')
    try:
        sector = get_object_or_404(Sector, name = sector_id)
        subsectors = sector.subsectors.all()
    except:
        subsectors = []
    subsectors_data = serialize('json', subsectors)
    print (f'---> subsectors for: {request.GET.get('sector')}: {subsectors.count()}')
    return render(request, 'partials/subsector_options.html', {'subsectors': subsectors})