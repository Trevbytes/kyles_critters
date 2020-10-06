from django.test import TestCase
from .models import Product, Category, SubCategory


class ProductModelTest(TestCase):
    """Test the product Model."""
    def test_string_representation(self):
        product = Product(name="Product Name")
        self.assertEqual(str(product), product.name)
        category = Category(friendly_name="Category Name")
        self.assertEqual(str(category), category.friendly_name)
        subcategory = SubCategory(friendly_name="Sub Name")
        self.assertEqual(str(subcategory), subcategory.friendly_name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Category._meta.verbose_name_plural), "Categories")
        self.assertEqual(str(SubCategory._meta.verbose_name_plural),
                         "Sub-Categories")


class ProductsPageTests(TestCase):
    """Test whether product entries show up on the products page."""

    def test_one_product(self):
        Product.objects.create(name='1-name',
                               description='&lt;p&gt;1-description\
                                    id.&lt;/p&gt;',
                               price=5.8)
        response = self.client.get('/products/')
        self.assertContains(response, '1-name')

    def test_two_products(self):
        Product.objects.create(name='1-name',
                               description='&lt;p&gt;1-description\
                                    id.&lt;/p&gt;',
                               price=4.5)
        Product.objects.create(name='2-name',
                               description='&lt;p&gt;2-description\
                                    id.&lt;/p&gt;',
                               price=1.0)
        response = self.client.get('/products/')
        self.assertContains(response, '1-name')
        self.assertContains(response, '2-name')


class ProductPageTest(TestCase):

    def test_product(self):

        """Test whether a product shows up on the product details page."""

        Product.objects.create(name='1-name',
                               description='&lt;p&gt;1-description\
                                    id.&lt;/p&gt;',
                               price=5.8)
        response = self.client.get('/products/1')
        # Client is redirected due to integer use in the url.
        self.assertEqual(response.status_code, 301)
