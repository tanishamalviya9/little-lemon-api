from django.test import TestCase
from restaurant.models import MenuItem, Booking


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title='IceCream', price=80, inventory=100)
        self.assertEqual(str(item), 'IceCream : 80')


class BookingTest(TestCase):
    def test_booking_str(self):
        booking = Booking.objects.create(
            name='Tanisha', no_of_guests=4, booking_date='2026-11-01T19:00:00Z'
        )
        self.assertEqual(str(booking), 'Tanisha')
