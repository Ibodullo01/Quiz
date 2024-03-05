
from django import template

register = template.Library()

@register.filter
def float_format(value , precision=3):
    return round(value , precision)
