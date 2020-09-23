from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order
from loan.models import LoanRequest


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.order_by('-date')
    loan_requests = profile.requests.order_by('-date')
    entries = profile.entries.order_by('-date')

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'form': form,
        'orders': orders,
        'loan_requests': loan_requests,
        'on_profile_page': True,
        'shuffled_entries': entries
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def request_history(request, order_number):
    loan_request = get_object_or_404(LoanRequest, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for request number {order_number}. '
        'A confirmation email was sent on the request date.'
    ))

    template = 'loan/request_success.html'
    context = {
        'loan_request': loan_request,
        'from_profile': True,
    }

    return render(request, template, context)
