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
            "class": "thumbnail inline", "format": "jpg", "crop": "fill", "height": 150, "width": 150, "use_root_path":True,
        },

        THUMBNAILTEST={
            "class": "thumbnail inline", "format": "jpg", "crop": "fill", "height": 300, "width": 300, "use_root_path":True,
        },
        CLOUDINARY_CLOUD_NAME=cloudinary.config().chickpeas
    )
