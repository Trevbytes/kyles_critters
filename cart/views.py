# Based on code taught by Code Institute
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the cart """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
    messages.success(request, f'Added {product.name} to your cart.')
    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """Update the quantity of the product"""

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0 and quantity < 21:
        cart[item_id] = quantity
        request.session['cart'] = cart
        messages.info(request, f'Updated quantity of {product.name}.')
    elif quantity < 1:
        cart.pop(item_id)
        request.session['cart'] = cart
        messages.warning(request, f'Removed {product.name} from your cart.')
    else:
        messages.error(request, f'{product.name} quantity must be 20 or less.')

    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove item from the cart"""

    product = Product.objects.get(pk=item_id)
    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)

        messages.warning(request, f'Removed {product.name} from your cart.')
        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
