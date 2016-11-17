import copy

from django import forms
from django.template.loader import render_to_string

from ..utils import dict_merge


class FuelUxWidgetMeta(forms.Widget.__class__):

    # def __new__(meta_class, name, bases, dic):
    #     return super().__new__(name, bases, dic)

    def __init__(cls, name, bases, dic):
        super().__init__(name, bases, dic)
        default_attrs = {}
        print("...............bases", bases)
        for base in reversed(bases):
            if hasattr(base, "default_attrs"):
                print("base", base)
                default_attrs = dict_merge(default_attrs, base.default_attrs)
        default_attrs = dict_merge(default_attrs, cls.default_attrs)
        cls.default_attrs = default_attrs


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
        self.attrs = self.dict_merge(self.default_attrs, self.attrs)

    # @classmethod
    def extend_default_attrs(self, default_attrs):
        return self.dict_merge(self.default_attrs, default_attrs)

    # @classmethod
    def dict_merge(self, dict1, dict2):
        """
        recursive update (not in-place).
        dict2 has precendence for equal keys.
        """
        dict1 = copy.deepcopy(dict1)

        for key in dict2:
            val = dict2[key]
            if type(val) is dict:
                # merge dictionaries
                if key in dict1 and type(dict1[key]) is dict:
                    dict1[key] = self.dict_merge(dict1[key], val)
                else:
                    dict1[key] = val
            else:
                dict1[key] = val
        return dict1

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
