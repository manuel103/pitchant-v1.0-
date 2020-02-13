from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import TemplateView
from pitchant.locations import views
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',include('pitchant.locations.urls')),
]
