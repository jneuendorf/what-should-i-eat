from django import forms
from django.template.loader import render_to_string

import copy


class FuelUxWidget(forms.Widget):
    """
    The super class for all fuel ux widgets.
    Documentation is missing. Source code at
    https://github.com/django/django/blob/master/django/forms/widgets.py.
    """

    template_name = None
    # list of attributes required for the widget to work
    required_attrs = []
    default_attrs = {}

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
