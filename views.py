from . import APP_NAME
from django.shortcuts import render
from .models import Tutorial


def index(request):
    return render(request, template_name="%s/view.html" % (APP_NAME),
                  context=dict(app_name=APP_NAME,
                               tutorials=Tutorial.objects.all()))
