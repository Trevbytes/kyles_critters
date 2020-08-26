from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):

    class Meta:
        verbose_name_plural = "Sub-Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)   

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sub_category = models.ForeignKey('SubCategory', null=True, blank=True,
                                     on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=False, blank=False)
    name = models.CharField(max_length=254, null=False, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # Points to a Cloudinary image
    # image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name
