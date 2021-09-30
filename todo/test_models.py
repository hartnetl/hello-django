from django.test import TestCase
from .models import Item

# Create your tests here.

class TestModels(TestCase):

    def test_done_default_false(self):
        # create an instance of an item and check its false
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)