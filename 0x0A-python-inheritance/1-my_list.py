#!/usr/bin/python3
"""
A subclass of list
print_sorted: Public instance  methods that sorts the list, ascending
Return: Sorted list
"""

class MyList(list):
    """
    Sort lisr in ascending order
    """
    def print_sorted(self):
        sorted_list = sorted(self)

        print(sorted_list)

