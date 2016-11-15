from .fuelux_widget import FuelUxWidget


class Datepicker(FuelUxWidget):
    """
    Widget for FuelUX's pillbox.
    See http://getfuelux.com/javascript.html#datepicker.

    Possible attributes:
    - auto_init
        - whether to add 'data-initialize="pillbox"'
    - id (required)
    - items (list of dictionaries with keys 'class', 'value' and 'text')
        - list of items that are already present in the pillbox
    - more
        - used to generate something like 'and 8 more'
        - more.before
        - more.after
    - add_item
        - placeholder text to display in the area the user has to click
          in order to add items
    - js (dictionary or boolean).
      Set this to False to take care ot the JavaScript yourself.
      The dictionary can contain any of the following keys:
        - acceptKeyCodes (list of integers)
        - edit (boolean)
        - readonly (boolean or -1)
        - truncate (boolean)
        - suggestions (list of strings)
      See FuelUX for more details.
    """

    template_name = "datepicker"
    default_attrs = {
        "auto_init": True,
        "month_names": [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ],
        "day_names_short": [
            "Su",
            "Mo",
            "Tu",
            "We",
            "Th",
            "Fr",
            "Sa",
        ],
        "today": "Today",
        "month_header": "Month",
        "year_header": "Year",
        "js": False
    }

    def use_required_attribute(self, initial):
        return False

    def set_suggestions(self, suggestions):
        if not suggestions.__iter__:
            raise ValueError(
                "Pillbox::set_suggestions: suggestions must be iterable."
            )
        print("my attrs ", self.attrs)
        self.attrs["js"]["suggestions"] = suggestions
        return self
