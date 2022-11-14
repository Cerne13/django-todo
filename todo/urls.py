from django.urls import path

from todo.views import (
    TaskListView,
    TaskCreateView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="todo-list"),
    path("create/", TaskCreateView.as_view(), name="task-create")
]


app_name = "todo"
