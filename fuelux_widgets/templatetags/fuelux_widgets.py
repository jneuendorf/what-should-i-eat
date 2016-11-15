from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


# @register.filter(name='slice')
@register.filter
@stringfilter
def slice(value, indices):
    '''
    Divides the value; argument is the divisor.
    Returns empty string on any error.
    '''
    [start, end] = [int(index) for index in indices.split(",")]
    return value[start:end]
