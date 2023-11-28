from django.shortcuts import render, redirect
from .models import Task


# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        obj = Task(name=name, priority=priority)
        obj.save()
    obj = Task.objects.all()
    return render(request, 'home.html', {'obj': obj})


def delete(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    obj = Task.objects.all()
    return render(request, 'delete.html', {'tsk': obj})
