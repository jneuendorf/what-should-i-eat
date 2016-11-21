from django import forms
from django.template.loader import render_to_string

from ..utils import dict_merge


class FuelUxWidgetMeta(type(forms.Widget)):

    def __init__(cls, name, bases, dic):
        super().__init__(name, bases, dic)
        default_attrs = {}
        required_attrs = set()
        for base in reversed(bases):
            if hasattr(base, "default_attrs"):
                default_attrs = dict_merge(default_attrs, base.default_attrs)
            if hasattr(base, "required_attrs"):
                # union
                required_attrs |= set(base.required_attrs)
        cls.default_attrs = dict_merge(default_attrs, cls.default_attrs)
        cls.required_attrs = list(required_attrs)


class FuelUxWidget(forms.Widget, metaclass=FuelUxWidgetMeta):
    """
    The super class for all fuel ux widgets.
    Documentation is missing. Source code at
    https://github.com/django/django/blob/master/django/forms/widgets.py.
    """

    template_name = None
    # list of attributes required for the widget to work
    required_attrs = []
    default_attrs = {
        "required": True,
    }

    def __init__(self, attrs={}):
        missing_required_attrs = []
        for required_attr in self.required_attrs:
            if not attrs.get(required_attr):
                missing_required_attrs.append(required_attr)

        if len(missing_required_attrs) > 0:
            # print("missing attrs: ", missing_required_attrs)
            raise ValueError(
                "FuelUxWidget requires the following attributes: {}."
                .format(", ".join(missing_required_attrs))
            )

        super().__init__(attrs)
        self.attrs = dict_merge(self.default_attrs, self.attrs)

    def render(self, name, value, attrs={}):
        return render_to_string(
            "fuelux_widgets/{}.html".format(self.template_name),
            self.build_attrs(attrs)
            # self.dict_merge(self.attrs, attrs)
        )

    # set name only if not passed in attrs (therefore contained in self.attrs)
    # (used in FuelUxForm)
    def set_name(self, name):
        if "name" not in self.attrs:
            self.attrs["name"] = name
        return self
