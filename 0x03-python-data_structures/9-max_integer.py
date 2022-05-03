#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    if len(my_list):
        for i in my_list:
            if i > max:
                max = i
        return max
    return None
