from django import template


register = template.Library()

@register.filter(name='div')
def div(value, arg):
    '''
    Divides the value; argument is the divisor.
    Returns empty string on any error.
    '''
    try:
        value = int(value)
        try:
            arg = len(list(arg))
        except:
            arg = int(arg)
        print(value)
        print(arg)
        if arg:
            return value / arg
    except Exception as e:
        # pass
        print(str(e))
    return ''
