from django.views.generic import TemplateView
from rest_framework import generics
# from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer


class HomePageView(TemplateView):
    template_name = 'ensaios/index.html'


# class TodoViewSet(viewsets.ModelViewSet):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer


class TodoListAndCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetailChangeAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
