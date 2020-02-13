from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse

from .models import Location
from .models import Department

from .forms import LocationForm, DepartmentForm

# Create your views here.


def location_list(request):
    locations = Location.objects.all()
    departments = Department.objects.all()

    context = {
        'locations': locations,
        'departments': departments,
    }
    return render(request, 'locations/location_list.html', context)


def save_location_form(request, form, template_name):
    data = dict()
    if request.method == 'POST' and request.url == '':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            locations = Location.objects.all()

            context = {
                'locations': locations
            }

            data['html_location_list'] = render_to_string('locations/includes/partial_location_list.html',
                                                          context)
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }

    data['html_form'] = render_to_string(
        template_name, context, request=request)
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
        data['html_form'] = render_to_string(
            'locations/includes/partial_location_delete.html', context, request=request)
    return JsonResponse(data)


# Departments section

def save_department_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            departments = Department.objects.all()

            context = {
                'departments': departments
            }

            data['html_department_list'] = render_to_string('locations/includes/partial_department_list.html',
                                                          context)
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }

    data['html_form'] = render_to_string(
        template_name, context, request=request)
    return JsonResponse(data)


def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
    else:
        form = DepartmentForm()
    return save_department_form(request, form, 'locations/includes/partial_department_create.html')

def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
    else:
        form = DepartmentForm(instance=department)
    return save_department_form(request, form, 'locations/includes/partial_department_update.html')

def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    data = dict()
    if request.method == 'POST':
        department.delete()
        data['form_is_valid'] = True
        departments = Department.objects.all()
        data['html_department_list'] = render_to_string('locations/includes/partial_department_list.html', {
            'departments': departments
        })
    else:
        context = {'department': department}
        data['html_form'] = render_to_string(
            'locations/includes/partial_department_delete.html', context, request=request)
    return JsonResponse(data)