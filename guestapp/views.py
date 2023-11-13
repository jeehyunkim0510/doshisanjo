from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from guestapp.forms import GuestCreationForm
from guestapp.models import Guest


# Create your views here.

class ArticleCreateView(CreateView):
    model = Guest
    form_class = GuestCreationForm
    template_name = 'guestapp/create.html'
    success_url = reverse_lazy('guestapp:list')

class ArticleUpdateView(UpdateView):
    model = Guest
    form_class = GuestCreationForm
    context_object_name = 'target_article'
    template_name = 'guestapp/update.html'
    success_url = reverse_lazy('guestapp:list')

class ArticleDeleteView(DeleteView):
    model = Guest
    form_class = GuestCreationForm
    context_object_name = 'target_article'
    template_name = 'guestapp/delete.html'
    success_url = reverse_lazy('guestapp:list')

class ArticleListView(ListView):
    model = Guest
    context_object_name = 'guest_list'
    template_name = 'guestapp/list.html'

def test(request):
    return render(request, 'guestapp/test.html')