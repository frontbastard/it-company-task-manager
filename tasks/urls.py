from django.urls import path

from tasks import views
from tasks.views import TaskListView

app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
]