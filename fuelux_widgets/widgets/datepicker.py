from .fuelux_widget import FuelUxWidget


class Datepicker(FuelUxWidget):
    """
    Widget for FuelUX's datepicker.
    See http://getfuelux.com/javascript.html#datepicker.

    Possible attributes:
    - auto_init (boolean)
        - whether to add 'data-initialize="datepicker"'
    - id (string)
    - style (string)
    - month_names (list of strings)
    - day_names_short (list of strings)
    - today (string)
    - prev_month (string)
    - next_month (string)
    - month (string)
    - year (string)
    - select (string)
    - back (string)
    - js (dictionary or boolean).
      Set this to False to take care ot the JavaScript yourself.
      The dictionary can contain any of the following keys:
        - allow_past_dates (boolean)
        - restricted (list)
        - moment_config (dictionary)
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
        "prev_month": "Previous Month",
        "next_month": "Next Month",
        "js": False,
        # for the "wheel" (when clicked on the month)
        "month": "Month",
        "year": "Year",
        "select": "Select",
        "back": "Return to Calendar",
    }

    def use_required_attribute(self, initial):
        return False
