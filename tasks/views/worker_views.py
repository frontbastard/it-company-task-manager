from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from tasks.models import Worker


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    paginate_by = 8

    def get_queryset(self):
        return super().get_queryset().exclude(is_superuser=True)


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    queryset = (Worker.objects.select_related("position")
                .prefetch_related("tasks"))
