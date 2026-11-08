from django.urls import reverse
from rest_framework.test import APITestCase

from .models import User


class UserListResponseTests(APITestCase):
    def test_admin_user_list_returns_an_array(self):
        admin = User.objects.create_user(
            username="admin",
            email="admin@example.com",
            password="test-password",
            role=User.Role.ADMIN,
        )
        self.client.force_authenticate(user=admin)

        response = self.client.get(reverse("user-list"))

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)
