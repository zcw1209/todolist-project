from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


# Create your views here.
def todolist(request):
    user = request.user
    todos = None
    if user.is_authenticated:
        todos = Todo.objects.filter(user=request.user).order_by("-created")
    print(todos)
    result = {"todos": todos, "user": user}
    return render(request, "todo/todolist.html", result)


def viewtodo(request, id):
    todo = None
    form = None
    message = ""
    try:
        todo = Todo.objects.get(id=id)

        if request.method == "GET":
            form = TodoForm(instance=todo)
        else:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            message = "修改成功!"

    except Exception as e:
        print(e)

    return render(
        request, "todo/viewtodo.html", {"todo": todo, "form": form, "message": message}
    )


def createtodo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()

        return redirect("todolist")
    else:
        form = TodoForm()

    form = TodoForm()
    return render(request, "todo/createtodo.html", {"form": form})
