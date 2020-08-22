from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import json
# Create your views here.

def index(request):
    return HttpResponse("TCorp demo")

def simpletemplate(request):
    context = {
        "variable1" : "Hello! This is a variabled passed to simple template.",
    }
    return render(request, 'myapp/simplet.html', context)

def demomodel(request):

    filtercolor = "blue"
    colors  = Color.objects.filter(color2=filtercolor)
    coloremployee  = Color.objects.filter(e__name="Phil")
    context = {
        'allemployee' : Employee.objects.all(),
        'colors' : colors,
        'coloremployee' : coloremployee,
    }
    return render(request, 'myapp/models.html', context)

def demoajax(request):
    if request.method == 'POST':
        if "userinput1" in request.POST:
            print(request.POST['userinput1'])
            return HttpResponse(request.POST['userinput1'])
        elif "userinput_dict" in request.POST:
            user_dict = json.loads(request.POST["userinput_dict"])
            print(user_dict["two"])
            print(user_dict["three"])
            return JsonResponse(user_dict)
    else:
        print("Get")
        context = {

        }
        return render(request, 'myapp/demoajax.html', context)
