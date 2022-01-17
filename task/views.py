from django.shortcuts import redirect, render
from .models import Task, TaskForm
import datetime

# Create your views here.

def list_task(request):
    tasks = Task.objects.all()
    date = datetime.date.today()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-task')
    else:
        form = TaskForm()
    return render(request, 'task/list_task.html', { 'tasks': tasks, 'form': form, 'date' : date })


def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('list-task')



