from django.test import Client, TestCase
from django.urls import reverse


class TestView(TestCase):
    def test_homepage(self):
        client = Client()

        response = client.get(reverse("index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<title>Holiday Homes</title>')
        self.assertTemplateUsed(response, "index.html")
