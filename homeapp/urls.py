from django.conf.urls.static import static
from django.urls import path

from homeapp.views import index, introduce, team
from mysite import settings

app_name='homeapp'

urlpatterns = [
    path('index/', index, name='index'),
    path('introduce/', introduce, name='introduce'),
    path('team/', team, name='team'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)