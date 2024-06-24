import os

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from dotenv import load_dotenv

from tasks.tests.factories import WorkerFactory, PositionFactory

load_dotenv()


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password=os.getenv("TEST_USER_PASSWORD")
        )
        self.client.force_login(self.admin_user)
        self.worker = WorkerFactory(position=PositionFactory())

    def test_position_listed(self):
        url = reverse("admin:tasks_worker_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.worker.position)

    def test_worker_detail_position_listed(self):
        url = reverse("admin:tasks_worker_change", args=[self.worker.id])
        res = self.client.get(url)
        self.assertContains(res, self.worker.position)
