import os
from django.contrib.auth import get_user_model

import factory
from dotenv import load_dotenv

from tasks.models import Position, Tag, TaskType, Task

load_dotenv()


class PositionFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: f"Test position {n}")

    class Meta:
        model = Position


class WorkerFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: f"Test username {n}")
    password = factory.PostGenerationMethodCall("set_password", os.getenv("SECRET_KEY"))
    position = factory.SubFactory(PositionFactory)

    class Meta:
        model = get_user_model()


class TagFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: f"Test tag {n}")

    class Meta:
        model = Tag


class TaskTypeFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: f"Test task type {n}")

    class Meta:
        model = TaskType


class TaskFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: f"Test name {n}")
    is_completed = False
    priority = factory.Iterator(Task.PriorityChoices.values)
    task_type = factory.SubFactory(TaskTypeFactory)

    @factory.post_generation
    def assignees(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for assignee in extracted:
                self.assignees.add(assignee)

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for tag in extracted:
                self.tags.add(tag)

    class Meta:
        model = Task
