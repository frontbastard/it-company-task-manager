from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from tasks.models import Task


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 8
