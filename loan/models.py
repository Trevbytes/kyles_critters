import uuid

from django.db import models
from django_countries.fields import CountryField
from products.models import Product
from profiles.models import UserProfile


class LoanRequest(models.Model):
    request_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='requests')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    critter_request = models.CharField(max_length=100, null=True, blank=True)
    request_info = models.TextField(null=True, blank=True)    
    date = models.DateTimeField(auto_now_add=True)

    def _generate_request_number(self):
        """
        Generate a random, unique request number using UUID
        """
        return uuid.uuid4().hex.upper()
    
    def __str__(self):
        return self.request_number