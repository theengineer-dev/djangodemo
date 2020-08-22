from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('simpletemplate', views.simpletemplate, name='simpletemplate'),
    path('demomodel', views.demomodel, name='demomodel'),
    path('demoajax', views.demoajax, name='demoajax'),
]
