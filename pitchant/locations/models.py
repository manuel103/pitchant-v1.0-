from django.db import models

# Create your models here.
class Location(models.Model):
    office_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    street_address = models.CharField(max_length=30)
    apt_suite = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    office_phone = models.CharField(max_length=50)
    
class Department(models.Model):
    department_name = models.CharField(max_length=50)
    department_code = models.CharField(max_length=20)
