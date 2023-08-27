from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_instance(self):
        menu = Menu.objects.create(
            title='IceCream',
            inventory=100,
            price=80
        )
        self.assertEqual(str(menu), 'IceCream: 80')