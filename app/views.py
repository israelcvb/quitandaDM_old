from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Produto
from .forms import ProdutoForm


def index(request):
    context = {
        'produtos': produtos,
    }
    return render(request, 'app/index.html', context)


def produto(request, produto_id):
    model = Produto
    template_name = 'app/produto.html'


class ProdutoList(ListView):
    model = Produto

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Lista de produtos'
        return context


class ProdutoDetail(DetailView):
    model = Produto

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        # return Produto.objects.select_related('nome').get(id=pk)
        return Produto.objects.get(id=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def produto_novo(request):
    form = ProdutoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'app/produto_novo.html', {'form':form})