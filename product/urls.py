from django.urls import path
from . import views


app_name = 'product'
urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index'),
    path('lista/', views.ProductListView.as_view(), name='list'),
    path('cadastro/', views.ProductCreateView.as_view(), name='create'),
    path('<int:pk>/detalhe/', views.ProductDetailView.as_view(), name='detail'),
    path('<int:pk>/atualizacao', views.ProductUpdateView.as_view(), name='update'),
    path('<int:pk>/exclusao', views.ProductDeleteView.as_view(), name='delete'),
]