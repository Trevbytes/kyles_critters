from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, SubCategory


def products(request):
    """ A view to return the products page """

    products = Product.objects.all()
    query = None
    category = None
    subcategory = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'sub_category' in request.GET:
            subcategories = request.GET['sub_category'].split(',')
            products = products.filter(sub_category__name__in=subcategories)
            subcategories = SubCategory.objects.filter(name__in=subcategories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query) | Q(sub_category__name__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_category': category,
        'current_subcategory': subcategory,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
