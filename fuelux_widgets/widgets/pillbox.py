from .fuelux_widget import FuelUxWidget


class Pillbox(FuelUxWidget):
    """
    Widget for FuelUX's pillbox.
    See http://getfuelux.com/javascript.html#pillbox.

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

    template_name = "pillbox"
    required_attrs = ["id"]
    default_attrs = {
        "auto_init": True,
        "add_item": "add item",
        "more": {
            "before": "and",
            "after": "more",
        },
        "js": {
            # "acceptKeyCodes": [13, 188]
            "edit": False
            # "suggestions": []

        }
    }
