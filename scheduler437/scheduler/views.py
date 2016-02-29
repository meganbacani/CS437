from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Major, Class


def index(request):
    return render(request,'scheduler/index.html')
