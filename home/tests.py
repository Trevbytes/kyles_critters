from django.test import TestCase


class ProductsPageTests(TestCase):

    """Test whether featured product entries show up on the home page."""

    def test_one_product(self):
        Product.objects.create(name='1-name', description='1-description', price=5.8, featured=True)
        response = self.client.get('/products/')
        self.assertContains(response, '1-name')
        self.assertContains(response, '1-description')

    def test_two_products(self):
        Product.objects.create(name='1-name', description='1-description', price=3.7, featured=True)
        Product.objects.create(name='2-name', description='2-description', price=1.0, featured=True)
        response = self.client.get('/products/')
        self.assertContains(response, '1-name')
        self.assertContains(response, '1-description')
        self.assertContains(response, '2-name')
