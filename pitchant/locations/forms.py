from django import forms

from .models import Location
from .models import Department

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('office_name', 'country', 'street_address', 'apt_suite', 'city', 'zip_code', 'office_phone',)


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ('department_name', 'department_code')