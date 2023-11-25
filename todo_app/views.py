from django.shortcuts import render
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
