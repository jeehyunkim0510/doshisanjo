from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'homeapp/index.html')

def introduce(request):
    return render(request, 'homeapp/introduce.html')

def team(request):
    return render(request, 'homeapp/team.html')

