#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements_printed = 0
    for i in range(0, x):
        try:
            print(f"{my_list[i]:d}", end="")
            elements_printed += 1
        except:
            pass
    print()
    return elements_printed
