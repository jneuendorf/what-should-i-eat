from django import forms

import fuelux_widgets


class FuelUxForm(forms.Form):

    # make widgets aware of their names
    # (make their name availabel in the render context)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            widget = self.fields[field_name].widget
            if isinstance(widget, fuelux_widgets.FuelUxWidget):
                widget.set_name(field_name)
