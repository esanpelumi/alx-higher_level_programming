#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict()
    leng = len(a_dictionary)
    for k, v in enumerate(a_dictionary):
        new_dict[v] = (a_dictionary[v]) * 2
    return new_dict
