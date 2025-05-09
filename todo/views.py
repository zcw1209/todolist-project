from django.shortcuts import render
from .models import Todo


# Create your views here.
def todolist(request):
    todos = Todo.objects.all()
    # get 唯一，filter 篩選
    # todos = Todo.objects.filter(id=1)

    print(todos)
    result = {"todos": todos}
    return render(request, "todo/todolist.html", result)


def viewtodo(request, id):
    todo = None
    try:
        todo = Todo.objects.get(id=id)
    except Exception as e:
        print(e)

    return render(request, "todo/viewtodo.html", {"todo": todo})
