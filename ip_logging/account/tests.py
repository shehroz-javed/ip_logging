from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth import get_user_model

User = get_user_model()


class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            email="testuser@gmail.com", password="testpass"
        )
        self.client.login(email="testuser@gmail.com", password="testpass")

    def test_home_view_redirect_for_logged_in_user(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_login_view_get(self):
        response = self.client.get(reverse("login"))
        self.assertTemplateUsed(response, "login.html")

    def test_login_view_post_valid(self):
        form_data = {"email": "testuser@gmail.com", "password": "testpass"}
        response = self.client.post(reverse("login"), form_data)
        self.assertRedirects(response, reverse("home"))
        self.assertTrue("_auth_user_id" in self.client.session)

    def test_login_view_post_invalid(self):
        form_data = {"email": "testuser@gmail.com", "password": "wrongpass"}
        response = self.client.post(reverse("login"), form_data)
        self.assertTemplateUsed(response, "login.html")
        self.assertContains(response, "Invalid username or password")

    def test_logout_view(self):
        self.client.logout()
        response = self.client.get(reverse("logout"))
        self.assertRedirects(response, reverse("login"))
        self.assertIsNone(self.client.session.get("_auth_user_id"))
