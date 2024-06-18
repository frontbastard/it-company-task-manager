from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from tasks.forms import TaskForm
from tasks.models import Task
from tasks.views.mixins import SearchableMixin


class TaskListView(
    LoginRequiredMixin,
    SearchableMixin,
    generic.ListView
):
    model = Task
    paginate_by = 8
    search_field = "name"


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    queryset = (Task.objects.select_related("task_type")
                .prefetch_related("assignees", "tags"))


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")
