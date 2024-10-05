from django.urls import path

from . import views


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("create/", views.TaskCreteView.as_view(), name="add-task"),
    path("update/<int:pk>/", views.TaskUpdateView.as_view(), name="update-task"),
    path("delete/<int:pk>/", views.TaskDeleteView.as_view(), name="delete-task"),
    path("tags/", views.TagListView.as_view(), name="tag-list"),
    path("tags/create/", views.TagCreateView.as_view(), name="tag-create"),
]

app_name = "todo_list_app"
