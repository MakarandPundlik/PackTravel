"""File containing django view tests for various user functionality"""
from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):
    """Test class to test Django views for various user functionality"""
    def setUp(self):
        """Tests for Client Setup"""
        self.client = Client()
        self.index_url = reverse("index")
        self.register_url = reverse("register")
        self.logout_url = reverse("logout")
        self.login_url = reverse("login")

    def test_index(self):
        """Tests for Client Index URL Validation"""
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200) # pylint: disable=deprecated-method
        self.assertTemplateUsed(response, "home/home.html")

    def test_register(self):
        """Tests for Client Register URL Validation"""
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200) # pylint: disable=deprecated-method
        self.assertTemplateUsed(response, "user/register.html")

    def test_login(self):
        """Tests for Client Login URL Validation"""
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200) # pylint: disable=deprecated-method
        self.assertTemplateUsed(response, "user/login.html")

    def test_logout(self):
        """Tests for Client Logout URL Validation"""
        response = self.client.post(self.login_url, {"username" : "ap", "password": "12345"})
        self.assertEquals(response.status_code, 302) # pylint: disable=deprecated-method
        response = self.client.get(self.logout_url)
        self.assertEquals(response.status_code, 302) # pylint: disable=deprecated-method
        self.assertRedirects(response, "/index/")

    def test_login_redirect(self):
        """Tests for Client Login URL Validation"""
        response = self.client.post(self.login_url, {"username" : "ap", "password": "12345" })
        self.assertEquals(response.status_code, 302) # pylint: disable=deprecated-method
        self.assertRedirects(response, "/index/ap")

    