#!/usr/bin/python3
"""
Class student with the attributes fist_name, last_name, and age

Initialized to attributes listed
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializing an instance of the class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self, attrs=None):
        """
        Retrieve dictionary representation of Student instance
        """
        if attrs is None:
            #  If attrs is None, retrieve all attribute
            obj_dict = {}
            for attr_name in dir(self):
                if not attr_name.startswith('_'):
                    attr_value = getattr(self, attr_name)
                    if isinstance(attr_value, (str, int, bool)):
                        obj_dict[attr_name] = attr_value
            return obj_dict
        else:
            #  If attrs is a list of strings, retrieve specified attributes
            obj_dict = {}
            for attr_name in attrs:
                if hasattr(self, attr_name):
                    attr_value = getattr(self, attr_name)
                    if isinstance(attr_value,  (str, int, bool)):
                        obj_dict[attr_name] = attr_value
            return obj_dict
