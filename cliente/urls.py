from django.urls import path

from cliente import views

app_name = 'cliente'
urlpatterns = [
    path('lista/', views.ClienteListView.as_view(), name='lista'),
    path('cadastro/', views.ClienteCreateView.as_view(), name='cadastro'),
    path('<int:pk>/detalhes/', views.ClienteDetailView.as_view(), name='detalhes'),
    path('<int:pk>/atualizacao/', views.ClienteUpdateView.as_view(), name='atualizacao'),
    path('<int:pk>/exclusao/', views.ClienteDeleteView.as_view(), name='exclusao'),
]