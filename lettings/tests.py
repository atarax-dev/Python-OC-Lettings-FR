from django.test import Client, TestCase
from django.urls import reverse

from lettings.models import Address, Letting


class TestView(TestCase):
    def test_lettings_page(self):
        client = Client()

        response = client.get(reverse("lettings:lettings_index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<title>Lettings</title>')
        self.assertTemplateUsed(response, "lettings/index.html")

    def test_context_data(self):
        client = Client()
        fake_address = Address.objects.create(
            number="25",
            street="Avenue Jean Jaurès",
            city="Nice",
            state="FR",
            zip_code="06100",
            country_iso_code="FRA",
        )
        Letting.objects.create(title="Fake Letting", address=fake_address)

        response = client.get(reverse("lettings:letting", kwargs={"letting_id": 1}))
        self.assertContains(response, '<title>Fake Letting</title>')
        self.assertContains(response, '<p>25 Avenue Jean Jaurès</p>')
