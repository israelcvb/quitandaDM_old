from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from cliente.models import Cliente


class IndexPageView(TemplateView):
    template_name = 'cliente/index.html'


class ClienteDetailView(DetailView):
    model = Cliente

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return Cliente.objects.get(pk=pk)


class ClienteListView(ListView):
    model = Cliente


class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nome', 'sexo', 'data_nascimento', 'cidade', 'bairro', 'fone', 'email', 'foto']

    def get_success_url(self):
        return reverse_lazy('cliente:lista')


class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nome', 'sexo', 'data_nascimento', 'cidade', 'bairro', 'fone', 'email', 'foto']

    def get_success_url(self):
        return reverse_lazy('cliente:lista')


class ClienteDeleteView(DeleteView):
    model = Cliente

    def get_success_url(self):
        return reverse_lazy('cliente:lista')
