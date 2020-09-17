from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import LoanRequestForm
from .models import LoanRequest
from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from django.db.models import Q

# Create your views here.


def loan(request):
    """ A view to return the loan a critter page """
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
            request_form = request_form.save(commit=False)
            request_form.save()
            return redirect(reverse('request_success',
                                    args=[request_form.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
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

    products = Product.objects.filter(Q(ready_to_loan=True))
    template = 'loan/loan_a_critter.html'
    context = {
        'request_form': request_form,
        'products': products,
    }

    return render(request, template, context)


def request_success(request, order_number):
    """
    Handle successful loan requests and send the user
    and store a confirmation email.
    """
    loan_request = get_object_or_404(LoanRequest, order_number=order_number)
    request_email = loan_request.email
    subject = render_to_string(
        'loan/confirmation_emails/confirmation_email_subject.txt',
        {'request': loan_request})
    body = render_to_string(
        'loan/confirmation_emails/confirmation_email_body.txt',
        {'request': loan_request,
         'contact_email': settings.DEFAULT_FROM_EMAIL})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [request_email]
    )

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [settings.DEFAULT_FROM_EMAIL]
    )

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        loan_request.user_profile = profile
        loan_request.save()

    messages.success(request, f'Request sent successfully! \
        Your request number is {order_number}. A confirmation \
        email will be sent to {loan_request.email}.')

    template = 'loan/request_success.html'
    context = {
        'loan_request': loan_request,
    }

    return render(request, template, context)
