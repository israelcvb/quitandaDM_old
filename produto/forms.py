from django.forms import CharField, Form, ModelForm, Textarea
from produto.models import Produto


class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['codigo', 'nome', 'fabricante', 'peso_bruto', 'unidade_peso', 'descricao', 'preco',
                  'data_fabricacao', 'unidade_medida']