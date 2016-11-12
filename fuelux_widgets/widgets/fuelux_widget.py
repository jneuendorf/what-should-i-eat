from django import forms
from django.template.loader import render_to_string


class FuelUxWidget(forms.Widget):
    """The super class for all fuel ux widgets."""

    template_name = None

    def render(self, name, value, attrs={}):
        # https://github.com/django/django/blob/master/django/forms/widgets.py
        # new_attrs = self.attrs.copy()
        # new_attrs.update(attrs)
        return render_to_string(
            "fuelux_widgets/{}.html".format(self.template_name),
            self.build_attrs(attrs)
        )
