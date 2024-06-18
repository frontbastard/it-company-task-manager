from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

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
