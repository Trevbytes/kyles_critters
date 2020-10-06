from django.db import models
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField


class Category(models.Model):

    class Meta:
        """Fix plural spelling error."""
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.friendly_name

    def get_friendly_name(self):
        return self.friendly_name


class SubCategory(models.Model):

    class Meta:
        """Fix plural spelling error."""
        verbose_name_plural = "Sub-Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)   

    def __str__(self):
        return self.friendly_name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sub_category = models.ForeignKey('SubCategory', null=True, blank=True,
                                     on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=False, blank=False)
    name = models.CharField(max_length=254, null=False, blank=False)
    description = RichTextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # Points to a Cloudinary image
    image = CloudinaryField('image', null=True, blank=True)
    featured = models.BooleanField(null=False, blank=False, default=False)
    ready_to_loan = models.BooleanField(null=False, blank=False, default=False)
    out_of_stock = models.BooleanField(null=False, blank=False, default=False) 
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name
