# Custom cart tool to calculate a subtotal. Code taught by Code Institute
from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
