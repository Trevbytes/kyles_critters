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

    if request.method == 'POST':

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'critter_request': request.POST['critter_request'],
            'request_info': request.POST['request_info'],
        }

        request_form = LoanRequestForm(form_data)
        if request_form.is_valid():
            request = request_form.save(commit=False)

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[request.request_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
