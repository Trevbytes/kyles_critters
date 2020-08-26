from django.test import TestCase

from .models import Product, Category, SubCategory


class ProductModelTest(TestCase):

    def test_string_representation(self):
        product = Product(name="Product Name")
        self.assertEqual(str(product), product.name)
        category = Category(friendly_name="Category Name")
        self.assertEqual(str(category), category.friendly_name)
        subcategory = SubCategory(friendly_name="Sub Name")
        self.assertEqual(str(subcategory), subcategory.friendly_name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Category._meta.verbose_name_plural), "Categories")
        self.assertEqual(str(SubCategory._meta.verbose_name_plural), "Sub-Categories")
