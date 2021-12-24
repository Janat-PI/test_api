from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import ToDo
from .serializers import ToDoSerializer


class ListToDo(ListAPIView):
    queryset = ToDo.objects.filter(is_published=True)
    serializer_class = ToDoSerializer


class DetailToDo(RetrieveAPIView):
    queryset = ToDo.objects.filter(is_published=True)
    serializer_class = ToDoSerializer


