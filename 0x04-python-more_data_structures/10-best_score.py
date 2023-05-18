#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        highest = list(a_dictionary.values())[0]
        for k, v in enumerate(a_dictionary):
            if a_dictionary[v] > highest:
                highest = a_dictionary[v]
            else:
                a_dictionary[v] = highest
        key_list = list(a_dictionary.keys())
        val_list = list(a_dictionary.values())
        position = val_list.index(highest)
        return key_list[position]
    else:
        return None
