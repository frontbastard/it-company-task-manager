from django import forms


class SearchForm(forms.Form):
    def __init__(self, *args, **kwargs):
        search_field = kwargs.pop("search_field", None)
        super().__init__(*args, **kwargs)
        self.fields[search_field] = forms.CharField(
            max_length=255,
            required=False,
            label="",
            widget=forms.TextInput(
                attrs={
                    "placeholder": f"Search by {search_field}"
                }
            )
        )