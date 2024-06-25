from django.contrib.auth import get_user_model
from django.test import TestCase

from django.urls import reverse

from tasks.tests.factories import WorkerFactory

WORKER_LIST_URL = reverse("tasks:worker-list")


class PublicWorkerTest(TestCase):
    def test_login_required(self):
        res = self.client.get(WORKER_LIST_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateWorkerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.worker = WorkerFactory(first_name="John", last_name="Doe")
        WorkerFactory(first_name="John", last_name="Smith")
        WorkerFactory(first_name="Chuck", last_name="Norris")

    def setUp(self):
        self.client.force_login(self.worker)

    def test_retrieve_tasks_list(self):
        res = self.client.get(WORKER_LIST_URL)
        self.assertEqual(res.status_code, 200)

        workers = get_user_model().objects.all()
        self.assertEqual(list(res.context["worker_list"]), list(workers))

    def test_search_tasks(self):
        res = self.client.get(WORKER_LIST_URL, {"first_name": "john"})
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "John")
        self.assertNotContains(res, "Chuck")
