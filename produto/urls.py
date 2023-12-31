from django.urls import path

from . import views

app_name = 'produto'
urlpatterns = [
    path("", views.IndexPageView.as_view(), name='index'),
    path("<int:pk>/detalhe", views.ProdutoDetailView.as_view(), name='detalhe'),
    path("lista/", views.ProdutoListView.as_view(), name='lista'),
    path("cadastro/", views.ProdutoCreateView.as_view(), name='cadastro'),
    path("<int:pk>/atualizacao/", views.ProdutoUpdateView.as_view(), name='atualizacao'),
    path("<int:pk>/exclusao/", views.ProdutoDeleteView.as_view(), name='exclusao'),
]