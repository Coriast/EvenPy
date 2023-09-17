from django.test import TestCase, Client
from django.urls import reverse
from event.models import Event, Conductor


class TestLogin(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_page(self):
        url = reverse("login")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class TestRegister(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_register_page(self):
        url = reverse("login")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class TestLogout(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_logout_page(self):
        url = reverse("logout")
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)


class TestEvent(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_event_page(self):
        url = reverse("event")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class TestConductor(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        Conductor.objects.create(
            username="jose", email="jose@email.com", password="123456"
        )

    def teste_create_conductor(self):
        person = Conductor.objects.get(username="jose")
        self.assertIsInstance(person, Conductor)

    # def teste_throw_create_organizer(self):
    #     person = Conductor.objects.exists()
    #     self.assertIsNotNone(person)
