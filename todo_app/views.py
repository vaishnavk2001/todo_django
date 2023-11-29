from django.shortcuts import render, redirect
from .models import Task
from .forms import Todoforms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy


# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        obj = Task(name=name, priority=priority, date=date)
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


def update(request, uid):
    task = Task.objects.get(id=uid)
    form = Todoforms(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'task': task, 'form': form})


# generic views(list)
class TaskListview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'obj'


# detailview
class TaskDetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'obj2'


# updateview
class TaskUpdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('details', kwargs={'pk': self.object.id})
