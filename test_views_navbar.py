from django.test import TestCase
from products.models import Product, Category, SubCategory


class TestViews(TestCase):

    def test_get_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_get_products(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_gallery(self):
        response = self.client.get('/gallery/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/gallery.html')

    def test_get_loan(self):
        response = self.client.get('/loan/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'loan/loan_a_critter.html')

    # Test that allauth is redirecting correctly
    def test_get_register_sign_in(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_get_profile(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_get_cart(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')

    def test_get_checkout(self):
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    def test_get_search_q(self):
        """ Test search function """
        Product.objects.create(name='Rat', description='1-description',
                               price=3.7)
        Product.objects.create(name='Mouse', description='2-description',
                               price=1.0)
        response = self.client.get('/products/?q=rat')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Rat')
        self.assertNotContains(response, 'Mouse')
        response2 = self.client.get('/products/?q=mouse')
        self.assertEqual(response2.status_code, 200)
        self.assertContains(response2, 'Mouse')
        self.assertNotContains(response2, 'Rat')

    def test_get_product_categories(self):
        """ Test search function """
        Product.objects.create(category=(Category.objects.create(
                                         name='critters',
                                         friendly_name='Critters')),
                               sub_category=(SubCategory.objects.create(
                                             name='pedigree_critters',
                                             friendly_name='Pedigree Critters')
                                             ),
                               name='Rat',
                               description='1-description',
                               price=3.7)
        Product.objects.create(category=(Category.objects.create(
                                         name='critters',
                                         friendly_name='Critters')),
                               sub_category=(SubCategory.objects.create(
                                             name='feeders',
                                             friendly_name='Feeders')
                                             ),
                               name='Mouse',
                               description='1-description',
                               price=3.7)
        Product.objects.create(category=(Category.objects.create(
                                         name='critters',
                                         friendly_name='Critters')),
                               sub_category=(SubCategory.objects.create(
                                             name='pedigree_critters',
                                             friendly_name='Pedigree Critters')
                                             ),
                               name='Chicken',
                               description='1-description',
                               price=5.7)
        Product.objects.create(category=(Category.objects.create(
                                         name='misc',
                                         friendly_name='Misc.')),
                               name='Dirt',
                               description='1-description',
                               price=1.0)
        response = self.client.get('/products/?q=critters')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Rat')
        self.assertNotContains(response, 'Dirt')
        response = self.client.get('/products/?q=feeders')
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Dirt')
        self.assertContains(response, 'Mouse')
