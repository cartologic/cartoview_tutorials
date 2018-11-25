from django.conf.urls import url

from . import APP_NAME, views

urlpatterns = urls = [url(r'^$', views.index, name="%s.index" % (APP_NAME)), ]
