from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import TemplateView
from pitchant.locations import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^locations/$', views.location_list, name='location_list'),
    url(r'^locations/create/$', views.location_create, name='location_create'),
    url(r'^locations/(?P<pk>\d+)/update/$', views.location_update, name='location_update'),
    url(r'^locations/(?P<pk>\d+)/delete/$', views.location_delete, name='location_delete'),
]
