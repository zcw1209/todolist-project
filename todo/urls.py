from django.urls import path
from .views import todolist, viewtodo, createtodo, deletetodo

urlpatterns = [
    path("", todolist, name="todolist"),
    path("view/<int:id>/", viewtodo, name="viewtodo"),
    path("create/", createtodo, name="createtodo"),
    path("delete/<int:id>/", deletetodo, name="deletetodo"),
]
