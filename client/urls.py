from django.urls import path
from . import views


app_name = 'client'

urlpatterns = [
    path('', views.ClientIndexView.as_view(), name='index'),
    path('lista/', views.ClientListView.as_view(), name='list'),
    path('<int:pk>/atualizacao/', views.ClientUpdateView.as_view(), name='update'),
    path('novo/', views.ClientCreateView.as_view(), name='new'),
    path('<int:pk>/detalhe/', views.ClientDetailView.as_view(), name='detail'),
    path('<int:pk>/exclusao/', views.ClientDeleteView.as_view(), name='delete'),
]
