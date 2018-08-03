from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    # url(r'^process/(?P<place>\w+)$', views.process),
    url(r'^/new$', views.new),
    url(r'^/create$', views.create),
    # url(r'^success$', views.success),
    # url(r'^reset$', views.reset),
    url(r'^/(?P<id>\d+)$', views.show),
    url(r'^/(?P<id>\d+)/edit$', views.edit),
    url(r'^/(?P<id>\d+)/update$', views.update),
    url(r'^/(?P<id>\d+)/delete$', views.destroy),
]