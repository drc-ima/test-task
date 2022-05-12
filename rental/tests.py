from django.test import TestCase

from rental.models import Rental

# Create your tests here.


class RentalTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.rental = Rental.objects.create(name='Rental - 1')

    def test_add_rental_view(self):

        response = self.client.post('/rental/add/', {'name': 'Rental 3'})

        self.assertEqual(response.status_code, 302, 'Success redirect')

    def test_reservations_view(self):

        response = self.client.get('')

        self.assertEqual(response.status_code, 200)

    def test_add_reservations_view(self):
        response = self.client.post('/reservation/add/', {'rental_id': self.rental.id, 'checkin': '2022-01-01', 'checkout': '2022-01-02'})

        self.assertEqual(response.status_code, 302)