from django.shortcuts import render
from django.views import generic

from todo.models import TodoItem


class TodoListView(generic.ListView):
    model = TodoItem
    template_name = "todo/todo_list.html"
    context_object_name = "todo_list"
