#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for x in my_list:
        if x % 2 == 0:
            x = True
            new_list.append(x)
        else:
            x = False
            new_list.append(x)
    return 
