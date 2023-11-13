from django.conf.urls.static import static
from django.urls import path

from homeapp.views import index, introduce, team
from mysite import settings
from testapp.views import test123

app_name='testapp'

urlpatterns = [
    path('test123/', test123, name='test123'),
    ]