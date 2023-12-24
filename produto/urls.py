from django.urls import path

from . import views

app_name = 'produto'
urlpatterns = [
    path("", views.IndexPageView.as_view(), name='index'),
    path("produto/<int:pk>/detalhe", views.ProdutoDetailView.as_view(), name='detalhe'),
    path("produto/lista/", views.ProdutoListView.as_view(), name='listar'),
    path("produto/cadastrar/", views.ProdutoCreateView.as_view(), name='cadastrar'),
    path("produto/<int:pk>/atualizar/", views.ProdutoUpdateView.as_view(), name='atualizar'),
    path("produto/<int:pk>/excluir/", views.ProdutoDeleteView.as_view(), name='excluir'),
]