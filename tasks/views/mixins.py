from django.db.models import Q
from django.views import generic

from tasks.forms import SearchForm


class SearchableMixin(generic.ListView):
    search_field = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_value = self.request.GET.get(self.search_field)
        context["search_form"] = SearchForm(
            search_field=self.search_field,
            initial={self.search_field: search_value}
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = SearchForm(self.request.GET, search_field=self.search_field)

        if form.is_valid():
            return queryset.filter(
                Q(**{f"{self.search_field}__icontains": form.cleaned_data[
                    self.search_field
                ]})
            )

        return queryset
