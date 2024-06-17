from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from tasks.models import Position


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    paginate_by = 8
