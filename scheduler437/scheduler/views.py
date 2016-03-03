from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.core import serializers
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
import sqlite3 as lite
import sys
import dateutil.parser
import time
import pytz
import json

from .models import Major, Class

def test(request):
    majors = []
    #try:
    #majorlist = Major.objects.all()
    #except Major.DoesNotExist:
     #   return HttpResponse("Something is breaking lol")

    #data = serializers.serialize('json', majorlist)
    #return HttpResponse({'data':data}, content_type="application/json")
    majorlist = Major.objects.all()
    for major in majorlist:
        name = major.majorName
        id = major.majorID
        majors.append({'name': name, 'id': id})
            
    #context = json.dumps(majors)
    #context = {'majors':  json.dumps(majors)}
    #context = {'home': {'majors':json.dumps(majors)}}
    #newcontext = json.dumps(context)
    
    
    question = get_object_or_404(Major, pk=1)
    return render(request, 'scheduler/index.html', {'question': question})
    
    #return HttpResponse(context, content_type="application/json")
    #return render(request, 'scheduler/index.html', context)

def index(request):
    majors = Major.objects.order_by('-majorName')[:5]
    template = loader.get_template('scheduler/index.html')
    context = {
        'majors': majors,
    }
    return HttpResponse(template.render(context, request))
    
def test2(request):
    majors = Major.objects.order_by('-majorName')[:5]
    template = loader.get_template('scheduler/index.html')
    context = {
        'majors': majors,
    }
    return HttpResponse(template.render(context, request))