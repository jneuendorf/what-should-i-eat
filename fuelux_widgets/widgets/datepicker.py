from .fuelux_widget import FuelUxWidget


class Datepicker(FuelUxWidget):
    """
    Widget for FuelUX's pillbox.
    See http://getfuelux.com/javascript.html#datepicker.

    Possible attributes:
    - auto_init
        - whether to add 'data-initialize="pillbox"'
    - id (required)
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
        self.attrs["js"]["suggestions"] = suggestions
        return self
