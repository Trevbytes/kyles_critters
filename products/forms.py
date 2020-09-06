from django import forms
from .models import Product, Category, SubCategory
from cloudinary.models import CloudinaryField


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = CloudinaryField('image', null=True, blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        sub_categories = SubCategory.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        friendly_names_s = [(s.id, s.get_friendly_name()) for s in sub_categories]

        self.fields['category'].choices = friendly_names
        self.fields['sub_category'].choices = friendly_names_s
