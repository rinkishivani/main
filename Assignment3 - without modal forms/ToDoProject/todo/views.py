from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from .models import ToDoList
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages


def home(request):
    tasks = ToDoList.objects.filter(deleted=False)
    return render(request, 'home.html', {'tasks': tasks })


def delete(request, pk):
    task = get_object_or_404(ToDoList, id=pk)
    task.delete()
    return redirect('/ToDoList/home/trash')

    # return render(request, 'confirm_delete.html', {'task': task})


def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        details = request.POST.get('details')
        if title:
            new_task = ToDoList.objects.create(title=title, details=details)
            return redirect('/ToDoList/home')

        else:
            messages.error(request, "Title cannot be empty. Please provide a title.")
    return render(request, 'create_task.html')


def update(request, pk):
    task = get_object_or_404(ToDoList, id=pk)
    if request.method == "POST":
        updated_title = request.POST.get('title')
        updated_details = request.POST.get('details')
        if updated_title:
            task.title = updated_title
            task.details = updated_details
            task.save()
            return redirect('/ToDoList/home')
        else:
            messages.error(request, "Title cannot be empty. Please provide a title.")
    return render(request, 'update_task.html', {'task': task})


def soft_delete(request, pk):
    task = get_object_or_404(ToDoList, id=pk)
    if request.method == "POST":
        task.deleted = True
        task.save()
        messages.error(request, "Moved to trash")
        return redirect('/ToDoList/home')

    return render(request, 'confirm_delete.html', {'task': task})


def trash(request):
    tasks = ToDoList.objects.filter(deleted=True)
    return render(request, 'trash.html', {'tasks': tasks})


def restore(request, pk):
    task = get_object_or_404(ToDoList, id=pk)
    task.deleted = False
    task.save()
    messages.error(request, "Restored")
    return redirect('/ToDoList/home')


def task(request, pk):
    tasks = ToDoList.objects.get(id=pk)
    return render(request, 'task.html', {'task': tasks})


