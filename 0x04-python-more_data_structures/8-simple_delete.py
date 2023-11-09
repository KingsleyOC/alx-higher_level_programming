#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary

# Example usage
my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_delete = 'b'
result_dict = simple_delete(my_dict, key_to_delete)
print(result_dict)
