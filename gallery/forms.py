from django import forms
from .models import GalleryEntry
from cloudinary.models import CloudinaryField


class GalleryEntryForm(forms.ModelForm):

    class Meta:
        """Uses Gallery Entry model."""
        model = GalleryEntry
        fields = '__all__'

    image = CloudinaryField('image', null=True, blank=True)
