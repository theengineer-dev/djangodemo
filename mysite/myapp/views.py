from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    return HttpResponse("TCorp demo")

def simpletemplate(request):
    context = {
        "variable1" : "Hello! This is a variabled passed to simple template.",
    }
    return render(request, 'myapp/simplet.html', context)

def demomodel(request):

    coloremployee  = Color.objects.filter(color="blue")
    context = {
        'allemployee' : Employee.objects.all(),
        'coloremployee' : coloremployee,
    }
    return render(request, 'myapp/models.html', context)
