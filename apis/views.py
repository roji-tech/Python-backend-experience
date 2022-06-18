from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from todos.models import Todo
from .serializers import TodoSerializer


class ListTodo(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Todo.objects.all()
#     serializer_class = TodoSerializer


# Create your views here.
