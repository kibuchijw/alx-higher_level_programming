#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        my_list = []
    for reversed_list in reversed(my_list):
        print("{:d}".format(reversed_list))
