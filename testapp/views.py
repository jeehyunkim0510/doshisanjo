from django.shortcuts import render

# Create your views here.

def test123(request):
    return render(request, 'testapp/test123.html')