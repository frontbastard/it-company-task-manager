from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from tasks.models import Worker, Position, Task


@login_required
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
