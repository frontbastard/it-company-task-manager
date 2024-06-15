from django.urls import path

from tasks import views
from tasks.views import (
    TaskListView,
    WorkerListView,
    PositionListView,
)

app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("positions/", PositionListView.as_view(), name="position-list"),
]