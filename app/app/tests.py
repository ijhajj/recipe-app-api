from django.test import TestCase
from app.calc import add, subtract


class CalcTest(TestCase):

    def test_add_numbers(self):
        """Test two numbers are added together properly in calc.add func"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """Values are subtracted and returned"""
        self.assertEqual(subtract(5, 11), 6)
