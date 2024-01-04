from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.


def index(request):
    item_list = Task.objects.order_by("created")
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid:
            form.save()
        return redirect("/")
    context = {"tasks": tasks, "forms": form,'list':item_list,'Title': "Todo App"}
    return render(request, "base/index.html", context)


def show(request):
    Tasks = Task.objects.all()
    context = {"Tasks": Tasks}
    return render(request, "base/show.html", context)



def remove(request, id):
    element = Task.objects.get(id=id)
    element.delete()
    messages.info(request, "Item deleted!")
    return redirect("/")
