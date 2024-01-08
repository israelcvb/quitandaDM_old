from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, TemplateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from product.models import Product


class IndexPageView(TemplateView):
    template_name = 'product/index.html'


class ProductListView(ListView):
    model = Product


class ProductCreateView(CreateView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return Product.objects.get(id=pk)
    

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['code', 'name', 'manufacturer', 'description', 'price', 'manufacturing_date']
    success_url = reverse_lazy("product:list")

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("product:list")