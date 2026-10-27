from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        user = User.objects.create_user('tester', password='pass12345')
        token = Token.objects.create(user=user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        MenuItem.objects.create(title='IceCream', price=80, inventory=100)
        MenuItem.objects.create(title='Pasta', price=120, inventory=50)

    def test_getall(self):
        response = self.client.get('/api/menu-items/')
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_requires_authentication(self):
        response = APIClient().get('/api/menu-items/')
        self.assertEqual(response.status_code, 401)

    def test_bookings_endpoint(self):
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, 200)
