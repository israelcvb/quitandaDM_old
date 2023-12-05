from django.forms import ModelForm
from .models import Produto


class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['codigo', 'nome', 'fabricante', 'peso_bruto', 'unidade_peso', 'descricao', 'preco',
                  'data_fabricacao', 'unidade_medida']