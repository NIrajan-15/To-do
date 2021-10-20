from django.shortcuts import render, redirect
from rest_framework import generics
from .models import *
from .forms import *
from .models import Task
from .serializers import TaskSerializer
# Create your views here.
class TaskView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

def main(request):
    tasks = Task.objects.all()

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


    
    context = {'tasks' : tasks, 'form' : form}
    return render(request, 'home.html', context)

def updateTask(request, pk):
    
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form' : form}

    return render(request, 'updates_task.html', context)

def deleteTask(request, pk):
    
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item' : item}
    return render(request, 'delete.html', context)