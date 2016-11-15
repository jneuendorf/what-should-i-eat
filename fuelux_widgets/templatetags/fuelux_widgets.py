from django import template
from django.template.defaultfilters import stringfilter

from json import dumps
from django.core.serializers.json import DjangoJSONEncoder


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


@register.filter(name='json')
def json(value):
    # print(str(value))
    try:
        return dumps(value, cls=DjangoJSONEncoder)
    except Exception as e:
        try:
            # assume models
            return dumps(list(value.values()), cls=DjangoJSONEncoder)
        except Exception as e:
            # pass
            print(str(e))
    return '{}'
