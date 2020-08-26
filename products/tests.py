from django.test import TestCase

from .models import Item


class EntryModelTest(TestCase):

    def test_string_representation(self):
        item = Item(name="Item Name")
        self.assertEqual(str(item), item.name)
