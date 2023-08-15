#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if 0 >= idx < len(my_list):
        return my_list

    list_copy = [i for i in my_list]
    list_copy[idx] = element
    return list_copy
