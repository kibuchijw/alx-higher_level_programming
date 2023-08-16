#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # new_list = my_list.copy()
    list_copy = [i for i in my_list]
    if 0 > idx >= len(my_list):
        return list_copy
    else:
        list_copy[idx] = element
        return list_copy
