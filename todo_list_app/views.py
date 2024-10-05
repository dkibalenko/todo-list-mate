from django.shortcuts import render
from django.views import generic

from .models import Task, Tag
from .forms import TaskForm

class IndexView(generic.ListView):
    template_name = "todo_list_app/index.html"
    model = Task
    context_object_name = "todo_list"
    queryset = Task.objects.order_by("done", "-datetime").prefetch_related("tags")


class TaskCreteView(generic.CreateView):
    template_name = "todo_list_app/task_form.html"
    model = Task
    form_class = TaskForm
    success_url = "/"


class TaskUpdateView(generic.UpdateView):
    template_name = "todo_list_app/task_form.html"
    model = Task
    form_class = TaskForm
    success_url = "/"


class TaskDeleteView(generic.DeleteView):
    template_name = "todo_list_app/task_confirm_delete.html"
    model = Task
    success_url = "/"


class TagListView(generic.ListView):
    template_name = "todo_list_app/tag_list.html"
    model = Tag
    context_object_name = "tag_list"
    queryset = Tag.objects.all()
