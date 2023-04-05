from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
# def index(request):
#     return render(request, 'todo_app/task_list.html')
from django.views import View
from django.views.generic import ListView

from .models import Task
from .forms import AddTaskForm


class TaskListView(ListView):
    """Вывод списка задач"""

    model = Task
    template_name = 'todo_app/task_list.html'

    def get_queryset(self):
        return Task.objects.all().order_by('create_at')


class AddTask(View):
    """Добавить задачу"""

    def post(self, request):
        form = AddTaskForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('task_list')


class DeleteTask(View):
    """Удалить задачу"""

    def get(self, request, pk):
        Task.objects.get(id=pk).delete()
        return redirect('task_list')


class UpdateStatus(View):
    """Обновить статус задачи"""

    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        if task.status:
            Task.objects.filter(id=pk).update(status=False)
        else:
            Task.objects.filter(id=pk).update(status=True)
        return redirect('task_list')
