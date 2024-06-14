from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.html import format_html

from tasks.models import Task, Position, Tag


@admin.register(get_user_model())
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("position",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "email",
                        "position",
                    )
                },
            ),
        )
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "deadline", "is_completed", "priority", "task_type", "tags_list", "assignees_list")
    search_fields = ("name",)
    list_filter = ("is_completed",)

    def tags_list(self, obj):
        return ", ".join([str(worker) for worker in obj.tags.all()])

    def assignees_list(self, obj):
        assignees = obj.assignees.all()
        if assignees:
            assignee_links = []
            for worker in assignees:
                assignee_links.append('<a href="{}">{}</a>'.format(
                    reverse('admin:%s_%s_change' % (worker._meta.app_label, worker._meta.model_name), args=(worker.pk,)),
                    str(worker)
                ))
            return format_html(", ".join(assignee_links))
        else:
            return "-"

    assignees_list.short_description = "Assignees"
    tags_list.short_description = "Tags"


admin.site.register(Position)
admin.site.register(Tag)
