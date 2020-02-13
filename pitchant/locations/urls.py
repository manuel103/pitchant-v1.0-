from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^locations/$', views.location_list, name='location_list'),
    url(r'^locations/create/$', views.location_create, name='location_create'),
    url(r'^locations/(?P<pk>\d+)/update/$', views.location_update, name='location_update'),
    url(r'^locations/(?P<pk>\d+)/delete/$', views.location_delete, name='location_delete'),

    url(r'^departments/create/$', views.department_create, name='department_create'),
    url(r'^departments/(?P<pk>\d+)/update/$', views.department_update, name='department_update'),
    url(r'^departments/(?P<pk>\d+)/delete/$', views.department_delete, name='department_delete'),
]