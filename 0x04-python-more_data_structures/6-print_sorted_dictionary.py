#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    emp = []
    for k, v in enumerate(a_dictionary):
        emp.append(v)
    new = sorted(emp)
    for x in range(len(a_dictionary)):
        print("{}: {}".format(new[x], a_dictionary[new[x]]))
