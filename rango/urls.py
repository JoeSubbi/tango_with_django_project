from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    #check if there is something after domain name
    #        if there is something call views.index
    #                     reference the view
    path('', views.index, name='index'),
]
