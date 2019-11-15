from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from .models import Task, Todo
from .froms import TodoForm


class TodoList(ListView):
    model = Todo
    template_name = 'list.html'


class AddTodo(FormView):
    form_class = TodoForm
    success_url = '/'
    template_name = 'add_todo.html'
