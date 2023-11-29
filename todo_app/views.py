from django.shortcuts import render, redirect
from .models import Task
from .forms import Todoforms


# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        obj = Task(name=name, priority=priority, date=date)
        obj.save()
    obj = Task.objects.all()
    return render(request, 'index.html', {'obj': obj})


def delete(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    obj = Task.objects.all()
    return render(request, 'delete.html', {'tsk': obj})


def update(request, uid):
    task = Task.objects.get(id=uid)
    form = Todoforms(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'task': task, 'form': form})
