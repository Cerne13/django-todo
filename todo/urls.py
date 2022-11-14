from django.urls import path

from todo.views import TodoListView

urlpatterns = [
    path("", TodoListView.as_view(), name="todo-list"),
]


app_name = "todo"
