from django.urls import path

from tasks.views.base import index
from tasks.views.position_views import PositionListView
from tasks.views.task_views import TaskListView, TaskDetailView
from tasks.views.worker_views import WorkerListView, WorkerDetailView

app_name = "tasks"

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
]