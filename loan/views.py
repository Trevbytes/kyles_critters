from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import LoanRequestForm

from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm

# Create your views here.


def loan(request):
    """ A view to return the loan a critter page """

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            request_form = LoanRequestForm(initial={
                'full_name': profile.user.get_full_name(),
                'email': profile.user.email,
                'phone_number': profile.default_phone_number,
                'country': profile.default_country,
                'street_address1': profile.default_street_address1,
                'street_address2': profile.default_street_address2,
                'town_or_city': profile.default_town_or_city,
                'county': profile.default_county,
                'postcode': profile.default_postcode,
            })
        except UserProfile.DoesNotExist:
            request_form = LoanRequestForm()
    else:
        request_form = LoanRequestForm()

    products = Product.objects.all()
    template = 'loan/loan_a_critter.html'
    context = {
        'request_form': request_form,
        'products': products,
    }

    return render(request, template, context)

