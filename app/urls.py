from django.urls import path
from .views import TodoList, AddTodo


urlpatterns = [
    path('add/', AddTodo.as_view(), name='add_todo'),
    path('', TodoList.as_view(), name='list')
]
