from django.test import TestCase
from .models import Order
from .forms import OrderForm


class CheckoutModelTest(TestCase):

    def setUp(self):
        Order.objects.create(order_number="123",
                             full_name="Test Name",
                             email="wer@eftim",
                             phone_number='252353',
                             country="test",
                             postcode="324",
                             town_or_city='test',
                             street_address1="234",
                             street_address2="wwer",
                             county="erw",
                             date="22/23/2000",
                             grand_total=22.44)

    def test_string_representation_order(self):
        order = Order.objects.get(full_name="Test Name")
        self.assertEqual(str(order), order.order_number)


class CheckoutFormTest(TestCase):

    def test_fields_are_explicit_in_form_metaclass(self):
        form = OrderForm()
        self.assertEqual(form.Meta.fields, ('full_name', 'email',
                                            'phone_number',
                                            'street_address1',
                                            'street_address2',
                                            'town_or_city', 'postcode',
                                            'country', 'county'))
