from . import views
from django.conf.urls import patterns, url
from . import APP_NAME
urlpatterns = urls = patterns('',
                              url(r'^$', views.index, name="%s.index" %
                                  (APP_NAME)),
                              )
