from django.shortcuts import render
from products.models import Product
from django.db.models import Q
# Create your views here.


def index(request):
    """ A view to return the index page """

    products = Product.objects.filter(Q(featured=True))
    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)
