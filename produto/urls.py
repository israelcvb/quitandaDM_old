from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path("", views.index, name='index'),
    path("<int:produto_id>/produto/", views.produto, name='produto'),
    path("produto/<int:pk>/detalhe", views.ProdutoDetail.as_view(), name='produto_detalhe'),
    path("produto/lista/", views.ProdutoList.as_view(), name='produto_lista'),
    path("produto/novo/", views.produto_novo, name='produto_novo'),
]