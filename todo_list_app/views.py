from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.views import generic

from .models import Task, Tag
from .forms import TaskForm, TagForm

class IndexView(generic.ListView):
    template_name = "todo_list_app/index.html"
    model = Task
    context_object_name = "todo_list"
    queryset = Task.objects.order_by("done", "-datetime") \
        .prefetch_related("tags")


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


class TagCreateView(generic.CreateView):
    template_name = "todo_list_app/tag_form.html"
    model = Tag
    form_class = TagForm
    success_url = "/"


class TagUpdateView(generic.UpdateView):
    template_name = "todo_list_app/tag_form.html"
    model = Tag
    form_class = TagForm
    success_url = "/"


class TagDeleteView(generic.DeleteView):
    template_name = "todo_list_app/tag_confirm_delete.html"
    model = Tag
    success_url = "/"


class ToggleDoneButton(generic.View):
    def post(self, request: HttpRequest, pk: int) -> HttpResponseRedirect:
        task = get_object_or_404(Task, pk=pk)
        task.done = not task.done
        task.save()
        return redirect("todo_list_app:index")
