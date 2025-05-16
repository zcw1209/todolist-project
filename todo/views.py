from django.shortcuts import render
from .models import Todo


# Create your views here.
def todolist(request):
    user = request.user
    todos = None
    if user.is_authenticated:
        todos = Todo.objects.filter(user=request.user)
    print(todos)
    result = {"todos": todos, "user": user}
    return render(request, "todo/todolist.html", result)


def viewtodo(request, id):
    todo = None
    try:
        todo = Todo.objects.get(id=id)
    except Exception as e:
        print(e)

    return render(request, "todo/viewtodo.html", {"todo": todo})
