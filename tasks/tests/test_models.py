from django.test import TestCase

from tasks.tests.factories import WorkerFactory, TaskFactory, PositionFactory, TaskTypeFactory, TagFactory


class ModelTests(TestCase):
    def setUp(self) -> None:
        self.worker = WorkerFactory()
        self.task = TaskFactory()
        self.position = PositionFactory()
        self.task_type = TaskTypeFactory()
        self.tag = TagFactory()

    def test_worker_str(self):
        self.assertEqual(
            str(self.worker),
            f"{self.worker.first_name} {self.worker.last_name}"
        )

    def test_task_str(self):
        self.assertEqual(str(self.task), self.task.name)

    def test_position_str(self):
        self.assertEqual(str(self.position), self.position.name)

    def test_task_type_str(self):
        self.assertEqual(str(self.task_type), self.task_type.name)

    def test_tag_str(self):
        self.assertEqual(str(self.tag), self.tag.name)
