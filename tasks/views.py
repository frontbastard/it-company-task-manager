from django.shortcuts import render
from django.views import generic

from tasks.models import Worker, Task, Position


def index(request):
    """View function for the home page of the site."""

    workers_num = Worker.objects.count()
    tasks_num = Task.objects.count()
    positions_num = Position.objects.count()

    visits_num = request.session.get("visits_num", 1)
    request.session["visits_num"] = visits_num + 1

    context = {
        "workers_num": workers_num,
        "tasks_num": tasks_num,
        "positions_num": positions_num,
        "visits_num": visits_num,
    }

    return render(request, "tasks/index.html", context=context)


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        priority_classes = {
            "urgent": "danger",
            "high": "warning",
            "normal": "primary",
            "low": "info",
        }

        for task in context["task_list"]:
            task.priority_class = priority_classes.get(task.priority, "info")

        return context
