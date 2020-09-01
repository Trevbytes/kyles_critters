from django.test import TestCase
from .forms import CartForm
from products.models import Product
# Create your tests here.


class AddToCartFormTest(TestCase):

    def setUp(self):
        self.entry = Product.objects.create(name='1-name',
                               description='1-description',
                               price=5.8)

    def test_init(self):
        CartForm(entry=self.entry)

    def test_valid_data(self):
        form = CartForm({
            'name': "1-name",
            'quantity': '2',
        }, entry=self.entry)
        self.assertTrue(form.is_valid())
        add_to_cart = form.save()
        self.assertEqual(add_to_cart.name, "1-name")
        self.assertEqual(add_to_cart.quantity, '2')
        self.assertEqual(add_to_cart.entry, self.entry)
