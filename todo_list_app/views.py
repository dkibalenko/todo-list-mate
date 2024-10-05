from django.shortcuts import render
from django.views import generic

from .models import Task, Tag

class IndexView(generic.ListView):
    template_name = "todo_list_app/index.html"
    model = Task
    context_object_name = "todo_list"
    queryset = Task.objects.order_by("done", "-datetime").prefetch_related("tags")
