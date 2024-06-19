from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views import generic, View

from tasks.forms import TaskForm
from tasks.models import Task
from tasks.views.mixins import SearchableMixin, SortableMixin


class TaskListView(
    LoginRequiredMixin,
    SearchableMixin,
    SortableMixin,
    generic.ListView
):
    model = Task
    paginate_by = 8
    search_field = "name"
    default_ordering = "name"
    sort_fields = [
        {"value": "name", "label": "Name asc"},
        {"value": "-name", "label": "Name desc"},
        {"value": "is_completed", "label": "Completed asc"},
        {"value": "-is_completed", "label": "Completed desc"},
    ]

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.get_ordering()
        if ordering:
            queryset = queryset.order_by(ordering)
        return queryset


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    queryset = (Task.objects.select_related("task_type")
                .prefetch_related("assignees", "tags"))


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = "tasks/confirm_delete.html"
    success_url = reverse_lazy("tasks:task-list")


class TaskToggleCompletionView(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_completed = not task.is_completed
        task.save()

        if task.is_completed:
            messages.success(request, "Task marked as completed.")
        else:
            messages.success(request, "Task marked as uncompleted.")

        return redirect("tasks:task-detail", pk=pk)
