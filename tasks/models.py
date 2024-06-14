from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        related_name="workers",
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        result = f"{self.first_name} {self.last_name}"

        if self.position:
            result += f" ({self.position.name})"

        return result

    class Meta:
        ordering = ["last_name", "first_name"]


class TaskType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Tag(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Task(models.Model):
    class PriorityChoices(TextChoices):
        URGENT = "urgent", "Urgent"
        HIGH = "high", "High"
        NORMAL = "normal", "Normal"
        LOW = "low", "Low"

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=10,
        choices=PriorityChoices.choices,
        default=PriorityChoices.NORMAL,
    )
    task_type = models.ForeignKey(
        TaskType,
        related_name="tasks",
        on_delete=models.PROTECT,
        null=True,
    )
    assignees = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="tasks",
        blank=True,
    )
    tags = models.ManyToManyField(
        Tag,
        related_name="tasks",
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["deadline"]
