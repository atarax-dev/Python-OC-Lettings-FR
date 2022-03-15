from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from profiles.models import Profile


class TestView(TestCase):
    def test_profiles_page(self):
        client = Client()

        response = client.get(reverse("profiles:profiles_index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<title>Profiles</title>')
        self.assertTemplateUsed(response, "profiles/index.html")

    def test_context_data(self):
        client = Client()
        fake_user = User.objects.create(username="FakeUser")
        Profile.objects.create(user=fake_user, favorite_city="Nice")

        response = client.get(reverse("profiles:profile", kwargs={"username": "FakeUser"}))
        self.assertContains(response, '<title>FakeUser</title>')
        self.assertContains(response, '<p>Favorite city: Nice</p>')