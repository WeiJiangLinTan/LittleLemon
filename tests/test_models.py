from django.test import TestCase
from restaurant import models

class MenuTest(TestCase):
    def test(self):
        item = models.Menu.objects.create(title="IceCream", price=80, inventory=100)
        itemstr = item.get_item()
        self.assertEqual(itemstr, "IceCream : 80")
        print("no working")
        
    def testtry(self):
        print("try")