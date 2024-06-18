from django import forms
from django.contrib.auth import get_user_model

from tasks.models import Task, Tag, TaskType


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
            ),
        )


class TaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local"}
        ),
        required=False,
    )
    task_type = forms.ModelChoiceField(
        queryset=TaskType.objects.all(),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.get("instance", None)
        super().__init__(*args, **kwargs)

        if self.instance is None:
            self.fields.pop("is_completed", None)
        else:
            pass

    class Meta:
        model = Task
        fields = ['name', 'description', 'deadline',
                  'priority', 'task_type', 'assignees', 'tags']
