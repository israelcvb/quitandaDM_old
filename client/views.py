from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, TemplateView, UpdateView
from django.views.generic.list import ListView
from .models import Client


class ClientIndexView(TemplateView):
    template_name = 'client/index.html'


class ClientListView(ListView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client

    fields = ['name', 'gender', 'birth_date', 'city', 'district', 'contact', 'email',
              'photo', 'cpf', 'last_purchase_date', 'status']
    

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return Client.objects.get(pk=pk)
    
    
    def get_success_url(self):
        return reverse_lazy('client:list')
    

class ClientCreateView(CreateView):
    model = Client
    fields = ['name', 'gender', 'birth_date', 'city', 'district', 'contact', 'email',
              'photo', 'cpf', 'last_purchase_date', 'status']

    def get_success_url(self) -> str:
        return reverse_lazy('client:list')
 

class ClientDetailView(DetailView):
    model = Client


class ClientDeleteView(DeleteView):
    model = Client

    def get_success_url(self):
        return reverse_lazy('client:list')