#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0

    try:
        for item in my_list:
            if count < x:
                print(item, end='')
                count += 1
    except IndexError:
        # If an IndexError occurs, break out of loop
        pass
    finally:
        # Print new line after printing elements
        print()
    return count
