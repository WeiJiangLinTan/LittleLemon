from django.test import TestCase

from restaurant.models import Menu

class MenuViewTest(TestCase):
    def testsetUptest(self) -> None:
        
        self.pizza = Menu.objects.create(title='Pizza', price=12.99, inventory=10)
        self.burger = Menu.objects.create(title='Burger', price=8.99, inventory=5)
        self.pasta = Menu.objects.create(title='Pasta', price=15.99, inventory=7)
    
    
    
    def test_getall(self):
        self.pasta = Menu.objects.create(title='Pasta', price=15.99, inventory=7)
