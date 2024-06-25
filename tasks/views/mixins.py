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
        context["search_field"] = self.search_field
        context["query_params"] = self.request.GET.copy()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = SearchForm(self.request.GET, search_field=self.search_field)

        if form.is_valid():
            search_value = form.cleaned_data[self.search_field]
            if search_value:
                return queryset.filter(
                    Q(**{f"{self.search_field}__icontains": search_value})
                )

        return queryset


class SortableMixin(generic.ListView):
    sort_fields = []
    default_ordering = None

    def get_ordering(self):
        ordering = self.request.GET.get("sort_by", self.default_ordering)
        valid_orderings = [field["value"] for field in self.sort_fields]
        if ordering in valid_orderings:
            return ordering
        return self.default_ordering

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sort_fields"] = self.sort_fields
        context["current_sort"] = self.request.GET.get(
            "sort_by", self.default_ordering
        )
        context["query_params"] = self.request.GET.copy()
        return context
