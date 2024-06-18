from django.urls import path

from tasks.views.base import index
from tasks.views.position_views import PositionListView
from tasks.views.task_views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
)
from tasks.views.worker_views import WorkerListView, WorkerDetailView

app_name = "tasks"

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("positions/", PositionListView.as_view(), name="position-list"),
]
