from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse

from .models import Location
from .forms import LocationForm

# Create your views here.
def location_list(request):
    locations = Location.objects.all()
    return render(request, 'locations/location_list.html', {'locations': locations})

def save_location_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            locations = Location.objects.all()
            data['html_location_list'] = render_to_string('locations/includes/partial_location_list.html', {
                'locations': locations
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def location_create(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
    else:
        form = LocationForm()
    return save_location_form(request, form, 'locations/includes/partial_location_create.html')


def location_update(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
    else:
        form = LocationForm(instance=location)
    return save_location_form(request, form, 'locations/includes/partial_location_update.html')

def location_delete(request, pk):
    location = get_object_or_404(Location, pk=pk)
    data = dict()
    if request.method == 'POST':
        location.delete()
        data['form_is_valid'] = True
        locations = Location.objects.all()
        data['html_location_list'] = render_to_string('locations/includes/partial_location_list.html', {
            'locations': locations
        })
    else:
        context = {'location': location}
        data['html_form'] = render_to_string('locations/includes/partial_location_delete.html', context, request=request)
    return JsonResponse(data)
