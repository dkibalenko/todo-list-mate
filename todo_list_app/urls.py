from django.urls import path

from . import views


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("create/", views.TaskCreteView.as_view(), name="add-task"),
]

app_name = "todo_list_app"
