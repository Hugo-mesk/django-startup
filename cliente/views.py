from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cliente.models import Client

class ClientList(ListView):
    model = Client
    template_name = 'client_list.html'

class ClientDetail(DetailView):
    model = Client
    template_name = 'client_detail.html'

class ClientCreate(CreateView):
    model = Client
    fields = ['fantasy_name', 'social_name', 'phone_number']
    template_name = 'client_create.html'
    success_url = reverse_lazy('client:client_list')

class ClientUpdate(UpdateView):
    model = Client
    fields = ['fantasy_name', 'social_name', 'phone_number']
    template_name = 'client_update.html'
    success_url = reverse_lazy('client:client_list')

class ClientDelete(DeleteView):
    model = Client
    template_name = 'client_delete.html'
    success_url = reverse_lazy('client:client_list')
