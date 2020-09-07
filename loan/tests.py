from django.test import TestCase
from .models import LoanRequest


class CheckoutModelTest(TestCase):

    def setUp(self):
        LoanRequest.objects.create(request_number="123",
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
                             request_info="Test info",
                             critter_request="mouse",)

    def test_string_representation_order(self):
        loan_request = LoanRequest.objects.get(full_name="Test Name")
        self.assertEqual(str(loan_request), loan_request.request_number)

class LoanFormTest(TestCase):

    def test_fields_are_explicit_in_form_metaclass(self):
        form = LoanRequestForm()
        self.assertEqual(form.Meta.fields, ('full_name', 'email',
                                            'phone_number',
                                            'street_address1',
                                            'street_address2',
                                            'town_or_city', 'postcode',
                                            'country', 'county',
                                            'request_info',
                                            'critter_request'))
