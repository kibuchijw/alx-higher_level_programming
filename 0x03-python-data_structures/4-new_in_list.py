#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    Prototype: def new_in_list(my_list, idx, element):
If idx is negative, the function should return a copy of the original list
If idx is out of range (> of number of element in my_list), the function should return a copy of the original list
You are not allowed to import any module
You are not allowed to use try/except
    if 0 >= idx < len(my_list):
    if 0 > idx >= len(my_list):
        return my_list
    list_copy = [i for i in my_list]
    list_copy[idx] = element
    return list_copy
