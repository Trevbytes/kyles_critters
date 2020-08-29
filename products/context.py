from products.models import Product


def all_critters(request):
    products = Product.objects.all()
    return {'all_critters': products}
