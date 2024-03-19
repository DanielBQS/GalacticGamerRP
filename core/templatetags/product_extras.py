from django import template

register = template.Library()

@register.filter()
def price_format(value):
    try:
        value = float(value)
        return '${0:,.0f}'.format(value)
    except ValueError:
        return value 