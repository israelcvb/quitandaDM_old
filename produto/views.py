from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from .models import Produto


class HomePageView(TemplateView):
    template_name = 'produto/home.html'


class ProdutoListView(ListView):
    model = Produto


class ProdutoDetailView(DetailView):
    model = Produto

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        # return Produto.objects.select_related('nome').get(id=pk)
        return Produto.objects.get(id=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ProdutoCreateView(CreateView):
    model = Produto
    fields = ["codigo", "nome", "preco", "descricao"]

    def get_success_url(self):
        return reverse_lazy('produto:listar')


class ProdutoDeleteView(DeleteView):
    model = Produto

    def get_success_url(self):
        return reverse_lazy('produto:listar')


class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = ["codigo", "nome", "preco", "descricao"]

    def get_success_url(self):
        return reverse_lazy('produto:listar')
