from django import forms

from products.models import Product


class CartForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'quantity')
