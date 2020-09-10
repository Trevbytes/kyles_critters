from django import forms
from products.models import Product
from .models import GalleryEntry
from cloudinary.models import CloudinaryField


class GalleryEntryForm(forms.ModelForm):

    class Meta:
        model = GalleryEntry
        fields = '__all__'

    image = CloudinaryField('image', null=True, blank=True)

