from rest_framework import generics, viewsets
from .serializers import TodoSerializer
from app.models import Todo


class TodoApiList(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
