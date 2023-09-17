#!/usr/bin/python3
"""
Convert an object instance to dictionary representation for JSON serialization
:param obj: Object instance to be converted
:return: Dictionaty representation of object
"""


def class_to_json(obj):
    """
    Function returning dictionary description with simple data structure
    """

    obj_dict = {}

    #  Iterate through object attributes
    for attr_name in dir(obj):
        #  Ignore private attributes
        if not attr_name.startswith('_'):
            attr_value = getattr(obj, attr_name)
            #  Check if attribute is serializable
            if isinstance(attr_value, (list, dict, str, int, bool)):
                #  Add attribute to dictionary representation
                obj_dict[attr_name] = attr_value

    return obj_dict
