from django.test import TestCase

from django.urls import reverse

from tasks.models import Position
from tasks.tests.factories import WorkerFactory, PositionFactory

POSITION_LIST_URL = reverse("tasks:position-list")


class PublicWorkerTest(TestCase):
    def test_login_required(self):
        res = self.client.get(POSITION_LIST_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateWorkerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.worker = WorkerFactory()
        PositionFactory(name="Java")
        PositionFactory(name="Javascript")
        PositionFactory(name="Python")

    def setUp(self):
        self.client.force_login(self.worker)

    def test_retrieve_tasks_list(self):
        res = self.client.get(POSITION_LIST_URL)
        self.assertEqual(res.status_code, 200)

        positions = Position.objects.all()
        self.assertEqual(list(res.context["position_list"]), list(positions))

    def test_search_tasks(self):
        res = self.client.get(POSITION_LIST_URL, {"name": "java"})
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Java")
        self.assertContains(res, "Javascript")
        self.assertNotContains(res, "Python")
