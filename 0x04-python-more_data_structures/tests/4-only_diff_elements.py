#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    difference = set() # Empty set to store elements

    for element in set_1:
        if element not in set_2:
            difference.add(element) # Add elements in set_1 but not available in set_2
    for  element in set_2:
        if element not in set_1:
            difference.add(element) # Addd elements in set_2 but not available in set_1
    return difference
