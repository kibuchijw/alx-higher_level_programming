#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    #  Sort the keys
    key_sort = sorted(a_dictionary.keys())

    for key in key_sort:
        print("{}: {}".format(key, a_dictionary[key]))
