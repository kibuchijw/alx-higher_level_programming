#!/usr/bin/python3
"""
Base class for managing id attribute in other classes
__nb_objects (int): Private class attribute
id (int): Public instance attribute
"""
import json


class Base:
    """
    Base class for managing id attribute in other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes new instance of Base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return JSON string of list of dictionaries
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write JSON string to file
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, mode='w', encoding='utf-8') as file:
            json_str = json.dumps([obj.to_dictionary() for obj in list_objs])
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Return dictionaris list from JSON
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create instance whose attributes are as per dictionary
        """
        if cls.__name__ == "Rectangle":
            #  Create dummy rectangle
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            #  Create dummy square
            dummy = cls(1)
        else:
            return None

        #  Use **kwargs and update method to apply values
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load instances from JSON file
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                json_str = file.read()
                if not json_str:
                    return []
                json_data = cls.from_json_string(json_str)
                return [cls.create(**item) for item in json_data]
        except FileNotFoundError:
            return []
