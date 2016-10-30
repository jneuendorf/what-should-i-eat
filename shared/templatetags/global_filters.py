from django import template
from json import dumps
from django.core.serializers.json import DjangoJSONEncoder


register = template.Library()

@register.filter(name='json')
def json(value):
    print(str(value))
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
