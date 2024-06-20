from parameterized import parameterized
from django.test import TestCase

from django.urls import reverse

from tasks.models import Task
from tasks.tests.factories import WorkerFactory, TaskFactory

TASK_LIST_URL = reverse("tasks:task-list")


class PublicTaskTest(TestCase):
    def test_login_required(self):
        res = self.client.get(TASK_LIST_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateTaskTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.worker = WorkerFactory()
        TaskFactory()
        TaskFactory()
        TaskFactory(name="Fake name")

    def setUp(self):
        self.client.force_login(self.worker)

    def test_retrieve_tasks_list(self):
        res = self.client.get(TASK_LIST_URL)
        self.assertEqual(res.status_code, 200)

        tasks = Task.objects.all().order_by("name")
        self.assertEqual(list(res.context["task_list"]), list(tasks))

    def test_search_tasks(self):
        res = self.client.get(TASK_LIST_URL, {"name": "test name"})
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Test name 0")
        self.assertContains(res, "Test name 1")
        self.assertNotContains(res, "Fake name")

    @parameterized.expand([
        ("name",),
        ("-name",),
        ("is_completed",),
        ("-is_completed",)
    ])
    def test_sort_tasks(self, sort_by):
        res = self.client.get(TASK_LIST_URL, {"sort_by": sort_by})
        self.assertEqual(res.status_code, 200)
        tasks = list(Task.objects.all().order_by(sort_by))
        self.assertEqual(list(res.context["task_list"]), tasks)

