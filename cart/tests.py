from django.test import TestCase
from .forms import CartForm
from products.models import Product
# Create your tests here.


class AddToCartFormTest(TestCase):

    def setUp(self):
        Product.objects.create(name='1-name',
                               description='1-description',
                               price=5.8)

    def test_init(self):
        CartForm(entry=self.name)
