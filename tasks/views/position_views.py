from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from tasks.models import Position
from tasks.views.mixins import SearchableMixin


class PositionListView(
    LoginRequiredMixin,
    SearchableMixin,
    generic.ListView
):
    model = Position
    paginate_by = 8
    search_field = "name"
