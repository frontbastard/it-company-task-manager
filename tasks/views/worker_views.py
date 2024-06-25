from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from tasks.models import Worker
from tasks.views.mixins import SearchableMixin


class WorkerListView(
    LoginRequiredMixin,
    SearchableMixin,
    generic.ListView,
):
    model = Worker
    paginate_by = 8
    search_field = "first_name"

    def get_queryset(self):
        return super().get_queryset().exclude(is_superuser=True)


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    queryset = (Worker.objects.select_related("position")
                .prefetch_related("tasks"))
