from products.models import Product
import cloudinary


def all_critters(request):
    products = Product.objects.all()
    return {'all_critters': products}


def images(request):
    return dict(
        ICON_EFFECTS=dict(
            format="png",
            type="facebook",
            transformation=[
                dict(height=95, width=95, crop="thumb", gravity="face", effect="sepia", radius=20),
                dict(angle=10),
            ]
        ),
        THUMBNAIL={
            "class": "thumbnail inline", "format": "jpg", "crop": "scale", "height": 170, "width": 300,
        },

        DETAIL_IMAGE={
            "class": "col-auto m-3 mb-auto p-0 card card-image img-fluid", "format": "jpg", "crop": "scale", "height": 300,
        },

        JUMBO={
            "crop": "fill", 'height': 300, "class": "jumbotron d-none d-md-block p-0 b-0 m-0 mb-2 card card-image img-fluid rounded mx-auto",
        },

        CARD={
            "class": "card-img-top rounded-top img-fluid", "format": "jpg", "crop": "scale", "alt": "Card image cap",
        },

        LOAN={
            "class": "grid-item p-2", "format": "jpg", "crop": "scale", "width": 200,
        },

        GALLERY={
            "format": "jpg", "crop": "scale", "width": 300,
        },
    )
