import copy


def dict_merge(dict1, dict2):
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
                dict1[key] = dict_merge(dict1[key], val)
            else:
                dict1[key] = val
        else:
            dict1[key] = val
    return dict1
