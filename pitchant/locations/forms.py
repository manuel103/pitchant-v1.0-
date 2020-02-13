from django import forms

from .models import Location


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('office_name', 'country', 'street_address', 'apt_suite', 'city', 'zip_code', 'office_phone',)

