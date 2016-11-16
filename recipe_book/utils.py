from shared import utils


def extract_ingredient_name(ingredient):
    # TODO: this should be moved to the database to be code independent
    units = [
        "pieces",
        "cups",
        "g",
        "kg",
        "l",
        "ml",
    ]

    words = ingredient.split()
    # 1 can of red hot chilli peppers -> red hot chilli peppers
    if "of" in ingredient:
        return ingredient.split("of ")[1]

    # examples:
    # two eggs -> eggs,
    # 1 tomato -> tomatoes,
    # 1 yellow carrot -> yellow carrots,
    # some sweet potatoes -> sweet potatoes
    # 20 g butter -> butter

    # pluralize last word
    if words[0] == "1" or words[0] == "one":
        words[-1:] = [utils.pluralize(" ".join(words[-1:]))]

    # ignore unit if contained
    if words[1] in units or utils.pluralize(words[1]) in units:
        index = 2
    else:
        index = 1
    return " ".join(words[index:])
