from django.urls import path

from homeapp.views import index, introduce, team

app_name='homeapp'

urlpatterns = [
    path('index/', index, name='index'),
    path('introduce/', introduce, name='introduce'),
    path('team/', team, name='team'),
    ]