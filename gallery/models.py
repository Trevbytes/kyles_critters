import uuid

from django.db import models
from products.models import Product
from profiles.models import UserProfile
from cloudinary.models import CloudinaryField


class GalleryEntry(models.Model):
    entry_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='entries')
    critter_name = models.CharField(max_length=50, null=False, blank=False)
    critter_type = models.ForeignKey(Product, null=True, blank=True,
                                 on_delete=models.SET_NULL)
    critter_info = models.TextField(null=True, blank=True)
    # Points to a Cloudinary image
    image = CloudinaryField('image', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def _generate_entry_number(self):
        """
        Generate a random, unique request number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.entry_number:
            self.entry_number = self._generate_entry_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.entry_number
