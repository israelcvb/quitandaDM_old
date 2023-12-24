from django.urls import path
# from rest_framework.routers import DefaultRouter
from . import views


# router = DefaultRouter()
# router.register('', views.TodoViewSet)
# urlpatterns = router.urls

app_name = 'ensaios'
urlpatterns = [
    path("", views.HomePageView.as_view(), name='index'),
    path("todo/", views.TodoListAndCreate.as_view(), name='ensaio_todo'),
    path("todo/<int:pk>/detail", views.TodoDetailChangeAndDelete.as_view(), name='ensaio_detail'),
]